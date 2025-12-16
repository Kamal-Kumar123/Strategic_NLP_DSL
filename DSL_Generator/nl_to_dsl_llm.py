import google.generativeai as genai
from config import GEMINI_API_KEY

class NLToDSLConverterLLM2:
    def __init__(self):
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel("models/gemma-3-12b-it")

    def convert(self, text: str) -> str:
        prompt = f"""
You are a STRICT compiler front-end.

Your task:
Convert the given natural language trading rules into a DSL.

⚠️ OUTPUT RULES (VERY IMPORTANT):
- Output ONLY valid DSL
- Do NOT explain anything
- Do NOT add extra text
- Follow the grammar EXACTLY

DSL GRAMMAR:
ENTRY:
<condition> [AND <condition>]*

EXIT:
<condition> [AND <condition>]*

CONDITION FORMAT:
<left> <operator> <right>

ALLOWED FIELDS:
close, open, high, low, volume

ALLOWED INDICATORS:
sma(close,N)
rsi(close,N)

DEFAULTS:
- If price is mentioned → use close
- If RSI period not specified → rsi(close,14)

COMPARISONS:
> < >= <= ==

EXAMPLES:
Natural Language:
"Buy when close is above 20 day moving average and volume above 1 million.
Exit when RSI below 30."

DSL:
ENTRY:
close > sma(close,20) AND volume > 1000000
EXIT:
rsi(close,14) < 30

NOW CONVERT THIS:

{text}
"""

        response = self.model.generate_content(prompt)
        return response.text.strip()
