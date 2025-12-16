🧠 Natural Language to Trading Strategy DSL

A lightweight end-to-end system that converts natural language trading strategies into a custom Domain-Specific Language (DSL), parses them into an Abstract Syntax Tree (AST), and executes a backtest on OHLCV market data.

This project demonstrates the full pipeline:
Natural Language → DSL → AST → Execution → Performance Metrics

✨ Features

🗣️ Natural Language Strategy Input

🧩 Custom Declarative Trading DSL

🌳 AST Construction with Boolean Logic

📊 Technical Indicators (SMA, RSI)

🔁 Entry & Exit Signal Evaluation

💹 Backtesting Engine with Metrics

🤖 Optional LLM Integration (Gemini / Gemma)

🏗️ Project Workflow
Natural Language Strategy
            ↓
      DSL Generation
            ↓
      AST Parsing
            ↓
 Entry / Exit Evaluation
            ↓
      Backtesting Engine
            ↓
   Trades & Performance Metrics


🛠️ Setup Instructions

1️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate      # Ubuntu / Mac
venv\Scripts\activate         # Windows

2️⃣ Configure LLM (Optional)

Create a .env file in the root directory:

GEMINI_API_KEY=your_api_key_here


Free Gemini API keys (limited tokens) can be used

Model Used: models/gemma-3-12b-it

LLM is optional — rule-based logic works without it

3️⃣ Dataset Configuration

Provide a path to an OHLCV CSV dataset
OR

Create a small custom dataset (example shown in main.py)

Supported fields:

open, high, low, close, volume

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Configure Inputs

In main.py:

Hardcode the natural language strategy

Set the dataset path or inline dataset

Example:

"Buy when close is above 20-day SMA and RSI is below 30.
 Exit when close falls below SMA."

6️⃣ Run the Project
python main.py      # Windows
python3 main.py     # Ubuntu

📥 Input & 📤 Output
✅ Input

Natural language trading strategy

OHLCV CSV market data

📌 Output

✔ Generated DSL

✔ Parsed Abstract Syntax Tree (AST)

✔ Entry / Exit signals

✔ Executed trades

✔ Backtest performance metrics (PnL, drawdown, etc.)

📄 Example Output
Generated DSL:
ENTRY:
close > sma(close, 20) AND rsi(close,14) < 30

EXIT:
close < sma(close, 20)

AST:
AND
 ├── close > sma(20)
 └── rsi < 30

🧩 Supported DSL Components
Indicators

sma(close, N)

rsi(close, N) (default N = 14)

Operators

>, <, >=, <=, ==

Boolean logic: AND, OR

📁 Project Structure (Suggested)
.
├── main.py
├── parser/
│   ├── grammar.py
│   ├── ast_builder.py
├── dsl/
│   ├── generator.py
├── backtest/
│   ├── engine.py
├── data/
│   └── sample.csv
├── requirements.txt
└── README.md

🎯 Use Cases

Academic DSL & compiler design projects

Algorithmic trading strategy prototyping

Natural language interfaces for trading systems

Research in NL → Program synthesis

🚀 Future Extensions

Support for more indicators (EMA, MACD, Bollinger Bands)

Strategy optimization & parameter tuning

Visualization of trades

Multiple asset backtesting

Risk management rules (SL / TP)

📜 License

This project is intended for educational and research purposes.