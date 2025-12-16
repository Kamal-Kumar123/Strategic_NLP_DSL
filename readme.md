# 🧠 Natural Language to Trading Strategy DSL

> Convert **human-readable trading strategies** into a **machine-executable trading DSL**, generate an **AST**, and run a **backtest** — end to end.

---

## 🚀 Overview

A lightweight yet powerful system that transforms **natural language trading ideas** into a **custom Domain-Specific Language (DSL)**, parses them into an **Abstract Syntax Tree (AST)**, and executes them on **OHLCV market data**.

Pipeline:

Natural Language → DSL → AST → Execution → Metrics

---

## ✨ Features

- 🗣️ Natural language strategy input  
- 🧩 Custom declarative trading DSL  
- 🌳 AST construction with boolean logic  
- 📊 Built-in indicators (SMA, RSI)  
- 🔁 Entry & exit signal evaluation  
- 💹 Backtesting engine with performance metrics  
- 🤖 Optional LLM support (Gemini / Gemma)  
- ⚡ Hybrid parsing (Regex → LLM fallback)

---

## 🏗️ System Flow

Strategy (Text)  
↓  
DSL Generator  
↓  
AST Builder  
↓  
Signal Evaluation  
↓  
Backtesting Engine  
↓  
Trades & Metrics  

---

## 🛠️ Setup

### 1️⃣ Create Virtual Environment

python -m venv venv  
source venv/bin/activate      # Linux / Mac  
venv\Scripts\activate         # Windows  

---

### 2️⃣ Configure LLM (Optional)

Create a `.env` file:

GEMINI_API_KEY=your_api_key_here  

Model: models/gemma-3-12b-it  
LLM is optional — rule-based parsing works without it.

---

### 3️⃣ Dataset

Provide an OHLCV CSV file or define a small inline dataset in `main.py`.

Required columns:

open, high, low, close, volume

---

### 4️⃣ Install Dependencies

pip install -r requirements.txt

---

### 5️⃣ Configure Strategy

Edit `main.py`:

Buy when close is above 20-day SMA and RSI is below 30.  
Exit when close falls below SMA.

---

### 6️⃣ Run Project

python main.py      # Windows  
python3 main.py     # Linux / Mac  

---

## 📥 Input & 📤 Output

Input:
- Natural language trading strategy  
- OHLCV market data  

Output:
- Generated DSL  
- Parsed AST  
- Entry / Exit signals  
- Executed trades  
- Performance metrics (PnL, drawdown)

---

## 📄 Example Output

Generated DSL:

ENTRY:  
close > sma(close, 20) AND rsi(close,14) < 30  

EXIT:  
close < sma(close, 20)  

AST:

AND  
├── close > sma(20)  
└── rsi < 30  

---

## 🧩 Supported DSL

Indicators:
- sma(close, N)
- rsi(close, N) (default N = 14)

Operators:
>, <, >=, <=, ==

Logic:
AND, OR

---

## 📁 Project Structure

Strategic_NLP_DSL/

├── AST_TO_CODE_Generation/  
│   └── code_generator.py  

├── Backtest_Engine/  
│   └── backtest.py  

├── DSL_Generator/  
│   ├── nl_to_dsl.py  
│   ├── nl_to_dsl_llm.py  
│   └── nl_to_dsl_hybrid.py  

├── DSL_To_AST_Generator/  
│   ├── ast_evaluator.py  
│   ├── dsl_parser.py  
│   └── indicators.py  

├── NLP_DSL/  

├── dataset.csv  
├── main.py  
├── config.py  
├── requirements.txt  
├── .env  
├── .gitignore  
├── Documentation.pdf  
└── README.md  

---

## 🎯 Use Cases

- DSL & compiler design projects  
- Algorithmic trading prototyping  
- Natural language program synthesis  
- AI-driven trading research  

---

## 🚧 Future Work

- More indicators (EMA, MACD, Bollinger Bands)  
- Strategy optimization  
- Trade visualization  
- Multi-asset support  
- Risk management (SL / TP)  

---

## 📜 License

Educational and research use only.
