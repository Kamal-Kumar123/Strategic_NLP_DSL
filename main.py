import pandas as pd
from DSL_Generator.nl_to_dsl_llm import NLToDSLConverterLLM2
from DSL_Generator.nl_to_dsl import NLToDSLConverter1
from DSL_To_AST_Generator.dsl_parser import DSLParser
from AST_To_CODE_Generation.code_generator import CodeGenerator
from Backtest_Engine.backtest import BacktestEngine
from DSL_Generator.nl_to_dsl_hybrid import NLToDSLHybrid
import json


# # 1. Dataset
# df = pd.read_csv("/home/kamal/Desktop/Strategic_NLP_DSL/dataset.csv")  # or build DataFrame inline as below

# sample data
data = {
    "datetime": [
        "2023-01-01",
        "2023-01-02",
        "2023-01-03",
        "2023-01-04",
        "2023-01-05",
        "2023-01-06",
        "2023-01-07",
        "2023-01-08",
        "2023-01-09",
        "2023-01-10",
        "2023-01-11",
        "2023-01-12",
        "2023-01-13",
        "2023-01-14",
        "2023-01-15",
        "2023-01-16",
    ],
    "open":   [100,102,104,106,108,110,112,114,116,118,120,118,115,112,108,105],
    "high":   [101,103,105,107,109,111,113,115,117,119,121,119,116,113,109,106],
    "low":    [99,101,103,105,107,109,111,113,115,117,119,117,114,111,107,104],
    "close":  [100,102,104,106,108,110,112,114,116,118,120,117,114,110,106,102],
    "volume": [
        800000,
        900000,
        1200000,  
        1300000,
        1250000,
        1400000,
        1500000,
        1600000,
        1550000,
        1700000,
        1800000,
        1600000,
        1400000,
        1300000,
        1200000,
        1100000
    ]
}



df = pd.DataFrame(data)


# 2. Natural language input
nl_text = """Buy when volume is above 1000000 and exit when RSI(2) is below 30.
"""

converter = NLToDSLHybrid()
dsl = converter.convert(nl_text)
print("DSL:\n", dsl)


# 4. DSL → AST       (input is simply DSL)
parser = DSLParser()
ast = parser.parse(dsl)
print(json.dumps(ast, indent=2))


# 5. AST → Signals               (input: dataframe === df   and AST)
generator = CodeGenerator(df)
signals = generator.generate_signals(ast)
print("Signals:\n", signals)



# 6. Backtest               (input: dataframe === df   and entry signal, exit signal)
engine = BacktestEngine(df)
results = engine.run(signals["entry"], signals["exit"])

print("Backtest Results:")
engine.pretty_print_trades(results["trades"])
