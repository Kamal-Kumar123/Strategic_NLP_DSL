import pandas as pd
from DSL_To_AST_Generator.ast_evaluator import ASTEvaluator

class CodeGenerator:
    def __init__(self, df):
        self.df = df
        self.evaluator = ASTEvaluator(df)

    def generate_signals(self, ast):
        entry_signal = self._build_logic(ast["entry"])
        exit_signal = self._build_logic(ast["exit"])

        return pd.DataFrame({
            "entry": entry_signal.fillna(False),
            "exit": exit_signal.fillna(False)
        })

    def _build_logic(self, node):
        # AND / OR logic
        if "op" in node:
            conditions = [
                self.evaluator.evaluate(cond)
                for cond in node["conditions"]
            ]

            if node["op"] == "AND":
                result = conditions[0]
                for c in conditions[1:]:
                    result = result & c
                return result

            if node["op"] == "OR":
                result = conditions[0]
                for c in conditions[1:]:
                    result = result | c
                return result

        # Single comparison
        return self.evaluator.evaluate(node)
