import pandas as pd
from DSL_To_AST_Generator.indicators import sma, rsi

class ASTEvaluator:
    def __init__(self, df):
        self.df = df

    def evaluate(self, node):
        """
        Entry point to evaluate any AST node
        """
        if node["type"] == "comparison":
            return self._eval_comparison(node)

        if node["type"] == "indicator":
            return self._eval_indicator(node)

        raise ValueError(f"Unknown node type: {node['type']}")

    def _eval_comparison(self, node):
        left = self._resolve(node["left"])
        right = self._resolve(node["right"])
        op = node["operator"]

        if op == ">":
            return left > right
        if op == "<":
            return left < right
        if op == ">=":
            return left >= right
        if op == "<=":
            return left <= right
        if op == "==":
            return left == right

        raise ValueError(f"Unsupported operator: {op}")

    def _eval_indicator(self, node):
        name = node["name"]
        args = node["args"]

        if name == "sma":
            return sma(self.df[args[0]], args[1])

        if name == "rsi":
            return rsi(self.df[args[0]], args[1])

        raise ValueError(f"Unknown indicator: {name}")

    def _resolve(self, value):
        """
        Resolve values like:
        - column name
        - number
        - indicator node
        """
        if isinstance(value, dict):
            return self.evaluate(value)

        if isinstance(value, str):
            return self.df[value]

        return value
