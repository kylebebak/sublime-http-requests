
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'documentAT BANG BRACE_L BRACE_R BRACKET_L BRACKET_R COLON DOLLAR EQUALS FALSE FLOAT_VALUE FRAGMENT INT_VALUE MUTATION NAME NULL ON PAREN_L PAREN_R QUERY SPREAD STRING_VALUE TRUE\n        document : definition_list\n        \n        document : selection_set\n        \n        document : selection_set fragment_list\n        \n        fragment_list : fragment_list fragment_definition\n        \n        fragment_list : fragment_definition\n        \n        definition_list : definition_list definition\n        \n        definition_list : definition\n        \n        definition : operation_definition\n                   | fragment_definition\n        \n        operation_definition : operation_type name variable_definitions directives selection_set\n        \n        operation_definition : operation_type name variable_definitions selection_set\n        \n        operation_definition : operation_type name directives selection_set\n        \n        operation_definition : operation_type name selection_set\n        \n        operation_definition : operation_type variable_definitions directives selection_set\n        \n        operation_definition : operation_type variable_definitions selection_set\n        \n        operation_definition : operation_type directives selection_set\n        \n        operation_definition : operation_type selection_set\n        \n        operation_type : QUERY\n                       | MUTATION\n        \n        selection_set : BRACE_L selection_list BRACE_R\n        \n        selection_list : selection_list selection\n        \n        selection_list : selection\n        \n        selection : field\n                  | fragment_spread\n                  | inline_fragment\n        \n        field : alias name arguments directives selection_set\n        \n        field : name arguments directives selection_set\n        \n        field : alias name directives selection_set\n        \n        field : alias name arguments selection_set\n        \n        field : alias name arguments directives\n        \n        field : name directives selection_set\n        \n        field : name arguments selection_set\n        \n        field : name arguments directives\n        \n        field : alias name selection_set\n        \n        field : alias name directives\n        \n        field : alias name arguments\n        \n        field : alias name\n        \n        field : name arguments\n        \n        field : name directives\n        \n        field : name selection_set\n        \n        field : name\n        \n        fragment_spread : SPREAD fragment_name directives\n        \n        fragment_spread : SPREAD fragment_name\n        \n        fragment_definition : FRAGMENT fragment_name ON type_condition directives selection_set\n        \n        fragment_definition : FRAGMENT fragment_name ON type_condition selection_set\n        \n        inline_fragment : SPREAD ON type_condition directives selection_set\n        \n        inline_fragment : SPREAD ON type_condition selection_set\n        \n        fragment_name : NAME\n                      | FRAGMENT\n                      | QUERY\n                      | MUTATION\n                      | TRUE\n                      | FALSE\n                      | NULL\n        \n        type_condition : named_type\n        \n        directives : directive_list\n        \n        directive_list : directive_list directive\n        \n        directive_list : directive\n        \n        directive : AT name arguments\n                  | AT name\n        \n        arguments : PAREN_L argument_list PAREN_R\n        \n        argument_list : argument_list argument\n        \n        argument_list : argument\n        \n        argument : name COLON value\n        \n        variable_definitions : PAREN_L variable_definition_list PAREN_R\n        \n        variable_definition_list : variable_definition_list variable_definition\n        \n        variable_definition_list : variable_definition\n        \n        variable_definition : DOLLAR name COLON type default_value\n        \n        variable_definition : DOLLAR name COLON type\n        \n        variable : DOLLAR name\n        \n        default_value : EQUALS const_value\n        \n        name : NAME\n             | FRAGMENT\n             | QUERY\n             | MUTATION\n             | ON\n             | TRUE\n             | FALSE\n             | NULL\n        \n        alias : name COLON\n        \n        value : variable\n              | INT_VALUE\n              | FLOAT_VALUE\n              | STRING_VALUE\n              | null_value\n              | boolean_value\n              | enum_value\n              | list_value\n              | object_value\n        \n        const_value : INT_VALUE\n                    | FLOAT_VALUE\n                    | STRING_VALUE\n                    | null_value\n                    | boolean_value\n                    | enum_value\n                    | const_list_value\n                    | const_object_value\n        \n        boolean_value : TRUE\n                      | FALSE\n        \n        null_value : NULL\n        \n        enum_value : NAME\n                   | FRAGMENT\n                   | QUERY\n                   | MUTATION\n                   | ON\n        \n        list_value : BRACKET_L value_list BRACKET_R\n                   | BRACKET_L BRACKET_R\n        \n        value_list : value_list value\n        \n        value_list : value\n        \n        const_list_value : BRACKET_L const_value_list BRACKET_R\n                         | BRACKET_L BRACKET_R\n        \n        const_value_list : const_value_list const_value\n        \n        const_value_list : const_value\n        \n        object_value : BRACE_L object_field_list BRACE_R\n                     | BRACE_L BRACE_R\n        \n        object_field_list : object_field_list object_field\n        \n        object_field_list : object_field\n        \n        object_field : name COLON value\n        \n        const_object_value : BRACE_L const_object_field_list BRACE_R\n                           | BRACE_L BRACE_R\n        \n        const_object_field_list : const_object_field_list const_object_field\n        \n        const_object_field_list : const_object_field\n        \n        const_object_field : name COLON const_value\n        \n        type : named_type\n             | list_type\n             | non_null_type\n        \n        named_type : name\n        \n        list_type : BRACKET_L type BRACKET_R\n        \n        non_null_type : named_type BANG\n                      | list_type BANG\n        '
    
_lr_action_items = {'MUTATION':([0,1,2,3,4,5,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,36,37,38,39,42,43,45,47,48,49,50,51,52,53,54,55,56,58,59,62,63,64,65,67,70,74,75,77,78,79,80,81,82,87,88,89,91,92,94,95,96,97,98,99,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,132,134,135,136,138,139,140,141,142,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,164,166,167,168,169,170,171,172,173,174,175,176,177,],[2,-7,-19,2,13,-8,32,-9,-18,13,-6,-75,-23,-78,-24,-77,-76,-73,-22,-74,-79,32,-41,-25,13,13,-72,-51,-53,-52,-49,-54,-48,-50,-56,13,-58,-17,-43,13,-38,13,-40,-39,-80,-20,-21,-37,13,-57,13,-16,-60,-15,-13,-42,-33,-32,-63,13,-31,-36,-34,-35,-59,-14,-11,-12,-47,-27,106,-62,-61,-30,-29,-28,-45,13,-10,-46,-104,-85,-99,-81,13,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,106,-64,13,-26,-44,13,13,-117,-115,106,-107,-109,-70,106,-116,-114,106,-106,-108,-93,13,-97,-94,-95,-96,-91,-90,-92,106,-118,-120,-122,13,106,-113,-111,106,-119,-121,-112,-110,-123,]),'FALSE':([2,4,7,9,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,36,37,38,39,42,43,47,48,49,50,51,52,53,54,55,56,58,59,62,64,70,74,75,77,78,79,80,81,82,87,92,94,95,96,97,98,99,100,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,134,135,136,138,139,140,141,142,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,164,166,167,168,169,170,171,172,173,174,175,176,177,],[-19,15,33,-18,15,-75,-23,-78,-24,-77,-76,-73,-22,-74,-79,33,-41,-25,15,15,-72,-51,-53,-52,-49,-54,-48,-50,-56,15,-58,-43,15,-38,15,-40,-39,-80,-20,-21,-37,15,-57,15,-60,-42,-33,-32,-63,15,-31,-36,-34,-35,-59,-47,-27,108,-62,-61,-30,-29,-28,15,-46,-104,-85,-99,-81,15,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,108,-64,15,-26,15,15,-117,-115,108,-107,-109,-70,108,-116,-114,108,-106,-108,-93,15,-97,-94,-95,-96,-91,-90,-92,108,-118,-120,-122,15,108,-113,-111,108,-119,-121,-112,-110,-123,]),'BRACE_L':([0,2,9,10,13,15,17,18,19,21,22,24,28,39,41,43,44,46,49,52,56,59,64,66,68,69,71,72,73,74,80,82,83,85,87,90,93,95,97,98,102,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,138,139,140,141,142,148,149,150,151,152,154,155,156,157,158,159,160,162,166,169,170,171,172,173,175,176,],[4,-19,-18,4,-75,-78,-77,-76,-73,-74,-79,4,-72,-56,4,-58,4,4,4,4,4,-57,-60,4,4,4,-127,-55,4,4,4,4,4,-65,-59,4,4,110,-61,4,4,-104,-85,-99,-81,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,110,-115,110,-107,-109,-70,153,-114,110,-106,-108,-93,-97,-94,-95,-96,-91,-90,-92,153,-120,153,-113,-111,153,-119,-112,-110,]),'TRUE':([2,4,7,9,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,36,37,38,39,42,43,47,48,49,50,51,52,53,54,55,56,58,59,62,64,70,74,75,77,78,79,80,81,82,87,92,94,95,96,97,98,99,100,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,134,135,136,138,139,140,141,142,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,164,166,167,168,169,170,171,172,173,174,175,176,177,],[-19,17,34,-18,17,-75,-23,-78,-24,-77,-76,-73,-22,-74,-79,34,-41,-25,17,17,-72,-51,-53,-52,-49,-54,-48,-50,-56,17,-58,-43,17,-38,17,-40,-39,-80,-20,-21,-37,17,-57,17,-60,-42,-33,-32,-63,17,-31,-36,-34,-35,-59,-47,-27,111,-62,-61,-30,-29,-28,17,-46,-104,-85,-99,-81,17,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,111,-64,17,-26,17,17,-117,-115,111,-107,-109,-70,111,-116,-114,111,-106,-108,-93,17,-97,-94,-95,-96,-91,-90,-92,111,-118,-120,-122,17,111,-113,-111,111,-119,-121,-112,-110,-123,]),'SPREAD':([4,13,14,15,16,17,18,19,20,21,22,24,25,26,28,32,33,34,35,36,37,38,39,43,47,49,51,52,54,55,56,59,64,70,74,75,79,80,81,82,87,92,94,97,98,99,100,105,127,],[23,-75,-23,-78,-24,-77,-76,-73,-22,-74,-79,-41,-25,23,-72,-51,-53,-52,-49,-54,-48,-50,-56,-58,-43,-38,-40,-39,-20,-21,-37,-57,-60,-42,-33,-32,-31,-36,-34,-35,-59,-47,-27,-61,-30,-29,-28,-46,-26,]),'BANG':([13,15,17,18,19,21,22,28,71,131,133,163,],[-75,-78,-77,-76,-73,-74,-79,-72,-127,144,146,-128,]),'PAREN_L':([2,9,10,13,15,17,18,19,21,22,24,28,46,56,64,],[-19,-18,40,-75,-78,-77,-76,-73,-74,-79,50,-72,40,50,50,]),'FLOAT_VALUE':([13,15,17,18,19,21,22,28,95,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,138,139,140,141,142,148,149,150,151,152,154,155,156,157,158,159,160,162,166,169,170,171,172,173,175,176,],[-75,-78,-77,-76,-73,-74,-79,-72,120,-104,-85,-99,-81,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,120,-115,120,-107,-109,-70,158,-114,120,-106,-108,-93,-97,-94,-95,-96,-91,-90,-92,158,-120,158,-113,-111,158,-119,-112,-110,]),'FRAGMENT':([0,1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,36,37,38,39,42,43,45,47,48,49,50,51,52,53,54,55,56,57,58,59,62,63,64,65,67,70,74,75,77,78,79,80,81,82,87,88,89,91,92,94,95,96,97,98,99,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,132,134,135,136,138,139,140,141,142,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,164,166,167,168,169,170,171,172,173,174,175,176,177,],[7,-7,-19,7,19,-8,7,35,-9,-18,19,-6,-75,-23,-78,-24,-77,-76,-73,-22,-74,-79,35,-41,-25,19,19,-72,-5,7,-51,-53,-52,-49,-54,-48,-50,-56,19,-58,-17,-43,19,-38,19,-40,-39,-80,-20,-21,-37,-4,19,-57,19,-16,-60,-15,-13,-42,-33,-32,-63,19,-31,-36,-34,-35,-59,-14,-11,-12,-47,-27,117,-62,-61,-30,-29,-28,-45,19,-10,-46,-104,-85,-99,-81,19,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,117,-64,19,-26,-44,19,19,-117,-115,117,-107,-109,-70,117,-116,-114,117,-106,-108,-93,19,-97,-94,-95,-96,-91,-90,-92,117,-118,-120,-122,19,117,-113,-111,117,-119,-121,-112,-110,-123,]),'PAREN_R':([13,15,17,18,19,21,22,28,60,61,71,77,78,84,96,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,122,123,125,129,130,131,133,136,139,141,143,144,146,148,150,152,154,155,156,157,158,159,160,161,163,166,171,173,176,],[-75,-78,-77,-76,-73,-74,-79,-72,-67,85,-127,-63,97,-66,-62,-104,-85,-99,-81,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,-64,-126,-69,-124,-125,-115,-107,-70,-68,-129,-130,-114,-106,-93,-97,-94,-95,-96,-91,-90,-92,-71,-128,-120,-111,-119,-110,]),'BRACE_R':([13,14,15,16,17,18,19,20,21,22,24,25,26,28,32,33,34,35,36,37,38,39,43,47,49,51,52,54,55,56,59,64,70,74,75,79,80,81,82,87,92,94,97,98,99,100,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,127,134,135,136,139,141,147,148,150,152,153,154,155,156,157,158,159,160,164,166,167,168,171,173,174,176,177,],[-75,-23,-78,-24,-77,-76,-73,-22,-74,-79,-41,-25,54,-72,-51,-53,-52,-49,-54,-48,-50,-56,-58,-43,-38,-40,-39,-20,-21,-37,-57,-60,-42,-33,-32,-31,-36,-34,-35,-59,-47,-27,-61,-30,-29,-28,-46,-104,-85,-99,-81,136,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,-26,148,-117,-115,-107,-70,-116,-114,-106,-93,166,-97,-94,-95,-96,-91,-90,-92,-118,-120,-122,173,-111,-119,-121,-110,-123,]),'QUERY':([0,1,2,3,4,5,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,36,37,38,39,42,43,45,47,48,49,50,51,52,53,54,55,56,58,59,62,63,64,65,67,70,74,75,77,78,79,80,81,82,87,88,89,91,92,94,95,96,97,98,99,100,101,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,132,134,135,136,138,139,140,141,142,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,164,166,167,168,169,170,171,172,173,174,175,176,177,],[9,-7,-19,9,21,-8,38,-9,-18,21,-6,-75,-23,-78,-24,-77,-76,-73,-22,-74,-79,38,-41,-25,21,21,-72,-51,-53,-52,-49,-54,-48,-50,-56,21,-58,-17,-43,21,-38,21,-40,-39,-80,-20,-21,-37,21,-57,21,-16,-60,-15,-13,-42,-33,-32,-63,21,-31,-36,-34,-35,-59,-14,-11,-12,-47,-27,119,-62,-61,-30,-29,-28,-45,21,-10,-46,-104,-85,-99,-81,21,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,119,-64,21,-26,-44,21,21,-117,-115,119,-107,-109,-70,119,-116,-114,119,-106,-108,-93,21,-97,-94,-95,-96,-91,-90,-92,119,-118,-120,-122,21,119,-113,-111,119,-119,-121,-112,-110,-123,]),'AT':([2,9,10,13,15,17,18,19,21,22,24,28,32,33,34,35,36,37,38,39,43,44,46,47,49,56,59,64,68,71,72,73,80,83,85,87,97,],[-19,-18,42,-75,-78,-77,-76,-73,-74,-79,42,-72,-51,-53,-52,-49,-54,-48,-50,42,-58,42,42,42,42,42,-57,-60,42,-127,-55,42,42,42,-65,-59,-61,]),'ON':([2,4,9,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,31,32,33,34,35,36,37,38,39,42,43,47,48,49,50,51,52,53,54,55,56,58,59,62,64,70,74,75,77,78,79,80,81,82,87,92,94,95,96,97,98,99,100,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,134,135,136,138,139,140,141,142,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,164,166,167,168,169,170,171,172,173,174,175,176,177,],[-19,18,-18,18,-75,-23,-78,-24,-77,-76,-73,-22,-74,-79,48,-41,-25,18,18,-72,58,-51,-53,-52,-49,-54,-48,-50,-56,18,-58,-43,18,-38,18,-40,-39,-80,-20,-21,-37,18,-57,18,-60,-42,-33,-32,-63,18,-31,-36,-34,-35,-59,-47,-27,116,-62,-61,-30,-29,-28,18,-46,-104,-85,-99,-81,18,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,116,-64,18,-26,18,18,-117,-115,116,-107,-109,-70,116,-116,-114,116,-106,-108,-93,18,-97,-94,-95,-96,-91,-90,-92,116,-118,-120,-122,18,116,-113,-111,116,-119,-121,-112,-110,-123,]),'INT_VALUE':([13,15,17,18,19,21,22,28,95,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,138,139,140,141,142,148,149,150,151,152,154,155,156,157,158,159,160,162,166,169,170,171,172,173,175,176,],[-75,-78,-77,-76,-73,-74,-79,-72,121,-104,-85,-99,-81,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,121,-115,121,-107,-109,-70,159,-114,121,-106,-108,-93,-97,-94,-95,-96,-91,-90,-92,159,-120,159,-113,-111,159,-119,-112,-110,]),'STRING_VALUE':([13,15,17,18,19,21,22,28,95,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,122,123,124,136,138,139,140,141,142,148,149,150,151,152,154,155,156,157,158,159,160,162,166,169,170,171,172,173,175,176,],[-75,-78,-77,-76,-73,-74,-79,-72,112,-104,-85,-99,-81,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,112,-115,112,-107,-109,-70,160,-114,112,-106,-108,-93,-97,-94,-95,-96,-91,-90,-92,160,-120,160,-113,-111,160,-119,-112,-110,]),'EQUALS':([13,15,17,18,19,21,22,28,71,129,130,131,133,144,146,163,],[-75,-78,-77,-76,-73,-74,-79,-72,-127,-126,142,-124,-125,-129,-130,-128,]),'BRACKET_R':([13,15,17,18,19,21,22,28,71,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,122,123,124,129,131,133,136,138,139,140,141,144,145,146,148,150,151,152,154,155,156,157,158,159,160,162,163,166,169,170,171,173,175,176,],[-75,-78,-77,-76,-73,-74,-79,-72,-127,-104,-85,-99,-81,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,139,-126,-124,-125,-115,150,-107,-109,-70,-129,163,-130,-114,-106,-108,-93,-97,-94,-95,-96,-91,-90,-92,171,-128,-120,176,-113,-111,-119,-112,-110,]),'COLON':([13,15,17,18,19,21,22,24,28,76,86,137,165,],[-75,-78,-77,-76,-73,-74,-79,53,-72,95,103,149,172,]),'BRACKET_L':([13,15,17,18,19,21,22,28,95,103,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,122,123,124,132,136,138,139,140,141,142,148,149,150,151,152,154,155,156,157,158,159,160,162,166,169,170,171,172,173,175,176,],[-75,-78,-77,-76,-73,-74,-79,-72,124,132,-104,-85,-99,-81,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,124,132,-115,124,-107,-109,-70,162,-114,124,-106,-108,-93,-97,-94,-95,-96,-91,-90,-92,162,-120,162,-113,-111,162,-119,-112,-110,]),'NULL':([2,4,7,9,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,36,37,38,39,42,43,47,48,49,50,51,52,53,54,55,56,58,59,62,64,70,74,75,77,78,79,80,81,82,87,92,94,95,96,97,98,99,100,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,134,135,136,138,139,140,141,142,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,164,166,167,168,169,170,171,172,173,174,175,176,177,],[-19,22,36,-18,22,-75,-23,-78,-24,-77,-76,-73,-22,-74,-79,36,-41,-25,22,22,-72,-51,-53,-52,-49,-54,-48,-50,-56,22,-58,-43,22,-38,22,-40,-39,-80,-20,-21,-37,22,-57,22,-60,-42,-33,-32,-63,22,-31,-36,-34,-35,-59,-47,-27,122,-62,-61,-30,-29,-28,22,-46,-104,-85,-99,-81,22,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,122,-64,22,-26,22,22,-117,-115,122,-107,-109,-70,122,-116,-114,122,-106,-108,-93,22,-97,-94,-95,-96,-91,-90,-92,122,-118,-120,-122,22,122,-113,-111,122,-119,-121,-112,-110,-123,]),'DOLLAR':([13,15,17,18,19,21,22,28,40,60,61,71,84,95,106,107,108,109,111,112,113,114,115,116,117,118,119,120,121,122,123,124,129,130,131,133,136,138,139,140,141,143,144,146,148,149,150,151,152,154,155,156,157,158,159,160,161,163,166,171,173,176,],[-75,-78,-77,-76,-73,-74,-79,-72,62,-67,62,-127,-66,126,-104,-85,-99,-81,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,126,-126,-69,-124,-125,-115,126,-107,-109,-70,-68,-129,-130,-114,126,-106,-108,-93,-97,-94,-95,-96,-91,-90,-92,-71,-128,-120,-111,-119,-110,]),'$end':([1,3,5,6,8,11,12,29,30,45,54,57,63,65,67,88,89,91,101,104,128,],[-7,-1,-8,-2,-9,0,-6,-5,-3,-17,-20,-4,-16,-15,-13,-14,-11,-12,-45,-10,-44,]),'NAME':([2,4,7,9,10,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,32,33,34,35,36,37,38,39,42,43,47,48,49,50,51,52,53,54,55,56,58,59,62,64,70,74,75,77,78,79,80,81,82,87,92,94,95,96,97,98,99,100,103,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,132,134,135,136,138,139,140,141,142,147,148,149,150,151,152,153,154,155,156,157,158,159,160,162,164,166,167,168,169,170,171,172,173,174,175,176,177,],[-19,28,37,-18,28,-75,-23,-78,-24,-77,-76,-73,-22,-74,-79,37,-41,-25,28,28,-72,-51,-53,-52,-49,-54,-48,-50,-56,28,-58,-43,28,-38,28,-40,-39,-80,-20,-21,-37,28,-57,28,-60,-42,-33,-32,-63,28,-31,-36,-34,-35,-59,-47,-27,123,-62,-61,-30,-29,-28,28,-46,-104,-85,-99,-81,28,-98,-84,-86,-89,-87,-105,-102,-88,-103,-83,-82,-100,-101,123,-64,28,-26,28,28,-117,-115,123,-107,-109,-70,123,-116,-114,123,-106,-108,-93,28,-97,-94,-95,-96,-91,-90,-92,123,-118,-120,-122,28,123,-113,-111,123,-119,-121,-112,-110,-123,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'fragment_name':([7,23,],[31,47,]),'object_value':([95,124,138,149,],[114,114,114,114,]),'fragment_spread':([4,26,],[16,16,]),'null_value':([95,124,138,142,149,162,169,172,],[107,107,107,152,107,152,152,152,]),'enum_value':([95,124,138,142,149,162,169,172,],[115,115,115,156,115,156,156,156,]),'default_value':([130,],[143,]),'argument':([50,78,],[77,96,]),'object_field':([110,134,],[135,147,]),'const_object_field_list':([153,],[168,]),'const_value_list':([162,],[169,]),'list_type':([103,132,],[133,133,]),'variable_definitions':([10,46,],[44,68,]),'value_list':([124,],[138,]),'type':([103,132,],[130,145,]),'directive':([10,24,39,44,46,47,49,56,68,73,80,83,],[43,43,59,43,43,43,43,43,43,43,43,43,]),'object_field_list':([110,],[134,]),'selection_set':([0,10,24,41,44,46,49,52,56,66,68,69,73,74,80,82,83,90,93,98,102,],[6,45,51,63,65,67,75,79,81,88,89,91,92,94,99,100,101,104,105,127,128,]),'value':([95,124,138,149,],[125,140,151,164,]),'argument_list':([50,],[78,]),'alias':([4,26,],[27,27,]),'boolean_value':([95,124,138,142,149,162,169,172,],[113,113,113,155,113,155,155,155,]),'name':([4,10,26,27,42,48,50,58,62,78,103,110,126,132,134,153,168,],[24,46,24,56,64,71,76,71,86,76,71,137,141,71,137,165,165,]),'arguments':([24,56,64,],[49,80,87,]),'definition':([0,3,],[1,12,]),'field':([4,26,],[14,14,]),'directive_list':([10,24,44,46,47,49,56,68,73,80,83,],[39,39,39,39,39,39,39,39,39,39,39,]),'fragment_list':([6,],[30,]),'inline_fragment':([4,26,],[25,25,]),'operation_definition':([0,3,],[5,5,]),'fragment_definition':([0,3,6,30,],[8,8,29,57,]),'list_value':([95,124,138,149,],[118,118,118,118,]),'non_null_type':([103,132,],[129,129,]),'directives':([10,24,44,46,47,49,56,68,73,80,83,],[41,52,66,69,70,74,82,90,93,98,102,]),'document':([0,],[11,]),'selection':([4,26,],[20,55,]),'selection_list':([4,],[26,]),'const_list_value':([142,162,169,172,],[157,157,157,157,]),'variable_definition':([40,61,],[60,84,]),'variable_definition_list':([40,],[61,]),'const_object_value':([142,162,169,172,],[154,154,154,154,]),'named_type':([48,58,103,132,],[72,72,131,131,]),'const_value':([142,162,169,172,],[161,170,175,177,]),'definition_list':([0,],[3,]),'operation_type':([0,3,],[10,10,]),'type_condition':([48,58,],[73,83,]),'variable':([95,124,138,149,],[109,109,109,109,]),'const_object_field':([153,168,],[167,174,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> document","S'",1,None,None,None),
  ('document -> definition_list','document',1,'p_document','parser.py',42),
  ('document -> selection_set','document',1,'p_document_shorthand','parser.py',48),
  ('document -> selection_set fragment_list','document',2,'p_document_shorthand_with_fragments','parser.py',54),
  ('fragment_list -> fragment_list fragment_definition','fragment_list',2,'p_fragment_list','parser.py',60),
  ('fragment_list -> fragment_definition','fragment_list',1,'p_fragment_list_single','parser.py',66),
  ('definition_list -> definition_list definition','definition_list',2,'p_definition_list','parser.py',72),
  ('definition_list -> definition','definition_list',1,'p_definition_list_single','parser.py',78),
  ('definition -> operation_definition','definition',1,'p_definition','parser.py',84),
  ('definition -> fragment_definition','definition',1,'p_definition','parser.py',85),
  ('operation_definition -> operation_type name variable_definitions directives selection_set','operation_definition',5,'p_operation_definition1','parser.py',97),
  ('operation_definition -> operation_type name variable_definitions selection_set','operation_definition',4,'p_operation_definition2','parser.py',108),
  ('operation_definition -> operation_type name directives selection_set','operation_definition',4,'p_operation_definition3','parser.py',118),
  ('operation_definition -> operation_type name selection_set','operation_definition',3,'p_operation_definition4','parser.py',128),
  ('operation_definition -> operation_type variable_definitions directives selection_set','operation_definition',4,'p_operation_definition5','parser.py',134),
  ('operation_definition -> operation_type variable_definitions selection_set','operation_definition',3,'p_operation_definition6','parser.py',144),
  ('operation_definition -> operation_type directives selection_set','operation_definition',3,'p_operation_definition7','parser.py',153),
  ('operation_definition -> operation_type selection_set','operation_definition',2,'p_operation_definition8','parser.py',162),
  ('operation_type -> QUERY','operation_type',1,'p_operation_type','parser.py',168),
  ('operation_type -> MUTATION','operation_type',1,'p_operation_type','parser.py',169),
  ('selection_set -> BRACE_L selection_list BRACE_R','selection_set',3,'p_selection_set','parser.py',175),
  ('selection_list -> selection_list selection','selection_list',2,'p_selection_list','parser.py',181),
  ('selection_list -> selection','selection_list',1,'p_selection_list_single','parser.py',187),
  ('selection -> field','selection',1,'p_selection','parser.py',193),
  ('selection -> fragment_spread','selection',1,'p_selection','parser.py',194),
  ('selection -> inline_fragment','selection',1,'p_selection','parser.py',195),
  ('field -> alias name arguments directives selection_set','field',5,'p_field_all','parser.py',201),
  ('field -> name arguments directives selection_set','field',4,'p_field_optional1_1','parser.py',208),
  ('field -> alias name directives selection_set','field',4,'p_field_optional1_2','parser.py',215),
  ('field -> alias name arguments selection_set','field',4,'p_field_optional1_3','parser.py',221),
  ('field -> alias name arguments directives','field',4,'p_field_optional1_4','parser.py',227),
  ('field -> name directives selection_set','field',3,'p_field_optional2_1','parser.py',233),
  ('field -> name arguments selection_set','field',3,'p_field_optional2_2','parser.py',239),
  ('field -> name arguments directives','field',3,'p_field_optional2_3','parser.py',245),
  ('field -> alias name selection_set','field',3,'p_field_optional2_4','parser.py',251),
  ('field -> alias name directives','field',3,'p_field_optional2_5','parser.py',257),
  ('field -> alias name arguments','field',3,'p_field_optional2_6','parser.py',263),
  ('field -> alias name','field',2,'p_field_optional3_1','parser.py',269),
  ('field -> name arguments','field',2,'p_field_optional3_2','parser.py',275),
  ('field -> name directives','field',2,'p_field_optional3_3','parser.py',281),
  ('field -> name selection_set','field',2,'p_field_optional3_4','parser.py',287),
  ('field -> name','field',1,'p_field_optional4','parser.py',293),
  ('fragment_spread -> SPREAD fragment_name directives','fragment_spread',3,'p_fragment_spread1','parser.py',299),
  ('fragment_spread -> SPREAD fragment_name','fragment_spread',2,'p_fragment_spread2','parser.py',305),
  ('fragment_definition -> FRAGMENT fragment_name ON type_condition directives selection_set','fragment_definition',6,'p_fragment_definition1','parser.py',311),
  ('fragment_definition -> FRAGMENT fragment_name ON type_condition selection_set','fragment_definition',5,'p_fragment_definition2','parser.py',318),
  ('inline_fragment -> SPREAD ON type_condition directives selection_set','inline_fragment',5,'p_inline_fragment1','parser.py',325),
  ('inline_fragment -> SPREAD ON type_condition selection_set','inline_fragment',4,'p_inline_fragment2','parser.py',332),
  ('fragment_name -> NAME','fragment_name',1,'p_fragment_name','parser.py',338),
  ('fragment_name -> FRAGMENT','fragment_name',1,'p_fragment_name','parser.py',339),
  ('fragment_name -> QUERY','fragment_name',1,'p_fragment_name','parser.py',340),
  ('fragment_name -> MUTATION','fragment_name',1,'p_fragment_name','parser.py',341),
  ('fragment_name -> TRUE','fragment_name',1,'p_fragment_name','parser.py',342),
  ('fragment_name -> FALSE','fragment_name',1,'p_fragment_name','parser.py',343),
  ('fragment_name -> NULL','fragment_name',1,'p_fragment_name','parser.py',344),
  ('type_condition -> named_type','type_condition',1,'p_type_condition','parser.py',350),
  ('directives -> directive_list','directives',1,'p_directives','parser.py',356),
  ('directive_list -> directive_list directive','directive_list',2,'p_directive_list','parser.py',362),
  ('directive_list -> directive','directive_list',1,'p_directive_list_single','parser.py',368),
  ('directive -> AT name arguments','directive',3,'p_directive','parser.py',374),
  ('directive -> AT name','directive',2,'p_directive','parser.py',375),
  ('arguments -> PAREN_L argument_list PAREN_R','arguments',3,'p_arguments','parser.py',382),
  ('argument_list -> argument_list argument','argument_list',2,'p_argument_list','parser.py',388),
  ('argument_list -> argument','argument_list',1,'p_argument_list_single','parser.py',394),
  ('argument -> name COLON value','argument',3,'p_argument','parser.py',400),
  ('variable_definitions -> PAREN_L variable_definition_list PAREN_R','variable_definitions',3,'p_variable_definitions','parser.py',406),
  ('variable_definition_list -> variable_definition_list variable_definition','variable_definition_list',2,'p_variable_definition_list','parser.py',412),
  ('variable_definition_list -> variable_definition','variable_definition_list',1,'p_variable_definition_list_single','parser.py',418),
  ('variable_definition -> DOLLAR name COLON type default_value','variable_definition',5,'p_variable_definition1','parser.py',424),
  ('variable_definition -> DOLLAR name COLON type','variable_definition',4,'p_variable_definition2','parser.py',430),
  ('variable -> DOLLAR name','variable',2,'p_variable','parser.py',436),
  ('default_value -> EQUALS const_value','default_value',2,'p_default_value','parser.py',442),
  ('name -> NAME','name',1,'p_name','parser.py',448),
  ('name -> FRAGMENT','name',1,'p_name','parser.py',449),
  ('name -> QUERY','name',1,'p_name','parser.py',450),
  ('name -> MUTATION','name',1,'p_name','parser.py',451),
  ('name -> ON','name',1,'p_name','parser.py',452),
  ('name -> TRUE','name',1,'p_name','parser.py',453),
  ('name -> FALSE','name',1,'p_name','parser.py',454),
  ('name -> NULL','name',1,'p_name','parser.py',455),
  ('alias -> name COLON','alias',2,'p_alias','parser.py',461),
  ('value -> variable','value',1,'p_value','parser.py',467),
  ('value -> INT_VALUE','value',1,'p_value','parser.py',468),
  ('value -> FLOAT_VALUE','value',1,'p_value','parser.py',469),
  ('value -> STRING_VALUE','value',1,'p_value','parser.py',470),
  ('value -> null_value','value',1,'p_value','parser.py',471),
  ('value -> boolean_value','value',1,'p_value','parser.py',472),
  ('value -> enum_value','value',1,'p_value','parser.py',473),
  ('value -> list_value','value',1,'p_value','parser.py',474),
  ('value -> object_value','value',1,'p_value','parser.py',475),
  ('const_value -> INT_VALUE','const_value',1,'p_const_value','parser.py',481),
  ('const_value -> FLOAT_VALUE','const_value',1,'p_const_value','parser.py',482),
  ('const_value -> STRING_VALUE','const_value',1,'p_const_value','parser.py',483),
  ('const_value -> null_value','const_value',1,'p_const_value','parser.py',484),
  ('const_value -> boolean_value','const_value',1,'p_const_value','parser.py',485),
  ('const_value -> enum_value','const_value',1,'p_const_value','parser.py',486),
  ('const_value -> const_list_value','const_value',1,'p_const_value','parser.py',487),
  ('const_value -> const_object_value','const_value',1,'p_const_value','parser.py',488),
  ('boolean_value -> TRUE','boolean_value',1,'p_boolean_value','parser.py',494),
  ('boolean_value -> FALSE','boolean_value',1,'p_boolean_value','parser.py',495),
  ('null_value -> NULL','null_value',1,'p_null_value','parser.py',501),
  ('enum_value -> NAME','enum_value',1,'p_enum_value','parser.py',507),
  ('enum_value -> FRAGMENT','enum_value',1,'p_enum_value','parser.py',508),
  ('enum_value -> QUERY','enum_value',1,'p_enum_value','parser.py',509),
  ('enum_value -> MUTATION','enum_value',1,'p_enum_value','parser.py',510),
  ('enum_value -> ON','enum_value',1,'p_enum_value','parser.py',511),
  ('list_value -> BRACKET_L value_list BRACKET_R','list_value',3,'p_list_value','parser.py',517),
  ('list_value -> BRACKET_L BRACKET_R','list_value',2,'p_list_value','parser.py',518),
  ('value_list -> value_list value','value_list',2,'p_value_list','parser.py',524),
  ('value_list -> value','value_list',1,'p_value_list_single','parser.py',530),
  ('const_list_value -> BRACKET_L const_value_list BRACKET_R','const_list_value',3,'p_const_list_value','parser.py',536),
  ('const_list_value -> BRACKET_L BRACKET_R','const_list_value',2,'p_const_list_value','parser.py',537),
  ('const_value_list -> const_value_list const_value','const_value_list',2,'p_const_value_list','parser.py',543),
  ('const_value_list -> const_value','const_value_list',1,'p_const_value_list_single','parser.py',549),
  ('object_value -> BRACE_L object_field_list BRACE_R','object_value',3,'p_object_value','parser.py',555),
  ('object_value -> BRACE_L BRACE_R','object_value',2,'p_object_value','parser.py',556),
  ('object_field_list -> object_field_list object_field','object_field_list',2,'p_object_field_list','parser.py',562),
  ('object_field_list -> object_field','object_field_list',1,'p_object_field_list_single','parser.py',570),
  ('object_field -> name COLON value','object_field',3,'p_object_field','parser.py',576),
  ('const_object_value -> BRACE_L const_object_field_list BRACE_R','const_object_value',3,'p_const_object_value','parser.py',582),
  ('const_object_value -> BRACE_L BRACE_R','const_object_value',2,'p_const_object_value','parser.py',583),
  ('const_object_field_list -> const_object_field_list const_object_field','const_object_field_list',2,'p_const_object_field_list','parser.py',589),
  ('const_object_field_list -> const_object_field','const_object_field_list',1,'p_const_object_field_list_single','parser.py',597),
  ('const_object_field -> name COLON const_value','const_object_field',3,'p_const_object_field','parser.py',603),
  ('type -> named_type','type',1,'p_type','parser.py',609),
  ('type -> list_type','type',1,'p_type','parser.py',610),
  ('type -> non_null_type','type',1,'p_type','parser.py',611),
  ('named_type -> name','named_type',1,'p_named_type','parser.py',617),
  ('list_type -> BRACKET_L type BRACKET_R','list_type',3,'p_list_type','parser.py',623),
  ('non_null_type -> named_type BANG','non_null_type',2,'p_non_null_type','parser.py',629),
  ('non_null_type -> list_type BANG','non_null_type',2,'p_non_null_type','parser.py',630),
]
