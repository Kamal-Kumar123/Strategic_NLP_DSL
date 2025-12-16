from lark import Lark, Transformer

grammar = r"""
start: entry_block exit_block

entry_block: "ENTRY:" condition
exit_block: "EXIT:" condition

condition: expr
         | expr "AND" expr   -> and_expr
         | expr "OR" expr    -> or_expr

expr: comparison

comparison: value OP value

value: INDICATOR
     | NAME
     | NUMBER

INDICATOR: NAME "(" NAME "," NUMBER ")"

OP: ">" | "<" | ">=" | "<=" | "=="

NAME: /[a-zA-Z_][a-zA-Z0-9_]*/
NUMBER: /\d+/

%import common.WS
%ignore WS
"""


class DSLTransformer(Transformer):

    def start(self, items):
        return {
            "entry": items[0],
            "exit": items[1]
        }

    def entry_block(self, items):
        return items[0]

    def exit_block(self, items):
        return items[0]

    def condition(self, items):
        return items[0]

    def expr(self, items):
        return items[0]

    def value(self, items):
        return items[0]

    def and_expr(self, items):
        return {
            "op": "AND",
            "conditions": items
        }

    def or_expr(self, items):
        return {
            "op": "OR",
            "conditions": items
        }

    def comparison(self, items):
        return {
            "type": "comparison",
            "left": items[0],
            "operator": str(items[1]),
            "right": items[2]
        }

    def INDICATOR(self, token):
        name, rest = str(token).split("(")
        args = rest.rstrip(")").split(",")
        return {
            "type": "indicator",
            "name": name,
            "args": [args[0], int(args[1])]
        }

    def NAME(self, token):
        return str(token)

    def NUMBER(self, token):
        return int(token)

class DSLParser:
    def __init__(self):
        self.parser = Lark(
            grammar,
            parser="lalr",
            transformer=DSLTransformer()
        )

    def parse(self, text):
        try:
            return self.parser.parse(text)
        except Exception as e:
            raise ValueError(f"DSL Syntax Error: {e}")
