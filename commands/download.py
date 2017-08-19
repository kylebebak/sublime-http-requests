import sublime
import sublime_plugin

import os

import requests

from .request import RequestsMixin
from ..core.helpers import truncate, absolute_path, get_transfer_indicator
from ..core.responses import Response
from ..core import RequestCommandMixin


class Download(RequestsMixin, RequestCommandMixin):
    """Download a file to disk without opening a response view.
    """
    CANCELLED = False

    def __init__(self, req):
        Download.CANCELLED = False
        self.config = sublime.load_settings('Requester.sublime-settings')
        self.req = req
        self.view = sublime.active_window().active_view()
        sublime.set_timeout_async(self.run_initial_request, 0)

    def run_initial_request(self):
        if self.req.method.lower() != 'get':
            sublime.error_message('Download Error: use "get" method to download files')
            return
        try:
            res = requests.get(*self.req.args, stream=True, **self.req.kwargs)
        except Exception as e:
            sublime.error_message('Download Error: {}'.format(e))
            return

        response = Response(self.req, res, None)
        self.handle_response(response)
        self.handle_responses([response])
        self.persist_requests([response])  # persist initial request before starting download

        if res.status_code != 200:
            sublime.error_message(
                'Download Error: response status code is not 200\n\n{}'.format(truncate(res.text, 500))
            )
            if sublime.load_settings('Requester.sublime-settings').get('only_download_for_200', True):
                return
        filename = self.req.skwargs.get('filename')
        sublime.set_timeout_async(lambda: self.download_file(res, filename), 0)

    def download_file(self, res, filename):
        filename = absolute_path(filename, self.view)
        if filename is None:
            sublime.error_message('Download Error: requester file must be saved to use relative path')
            return

        view = sublime.active_window().active_view()  # show download indicator in newly opened response tab
        length = int(res.headers.get('content-length') or 0)
        chunk_size = sublime.load_settings('Requester.sublime-settings').get('chunk_size', 1024)
        chunk_size = max(int(chunk_size), 128)
        chunk_count = 0
        basename = os.path.basename(filename)

        try:
            with open(filename, 'xb') as f:  # don't overwrite file if it already exists
                for chunk in res.iter_content(chunk_size):
                    if self.CANCELLED:
                        break
                    f.write(chunk)
                    chunk_count += 1
                    view.set_status('requester.download', 'Requester Download: {}'.format(
                        get_transfer_indicator(basename, chunk_count*chunk_size, length)
                    ))
            if self.CANCELLED:
                view.set_status('requester.download', 'Requester Download Cancelled: {}'.format(filename))
                os.remove(filename)
            else:
                view.set_status('requester.download', 'Requester Download Completed: {}'.format(filename))
        except Exception as e:
            sublime.error_message('Download Error: {}'.format(e))


class RequesterCancelDownloadsCommand(sublime_plugin.ApplicationCommand):
    """Cancel all outstanding downloads.
    """
    def run(self):
        Download.CANCELLED = True
