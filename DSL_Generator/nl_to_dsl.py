import re

class NLToDSLConverter1:

    def convert(self, text: str) -> str:
        text = text.lower()

        entry_rules = []
        exit_rules = []

        # ---------------- SMA ----------------
        sma_match = re.search(
            r"(\d+)\s*[-]?\s*day[s]?\s+moving\s+average",
            text
        )
        if sma_match:
            window = int(sma_match.group(1))

            if re.search(r"above|higher than|greater than|exceeds", text):
                entry_rules.append(f"close > sma(close,{window})")
            elif re.search(r"below|lower than|less than", text):
                entry_rules.append(f"close < sma(close,{window})")

        # ---------------- VOLUME ----------------
        volume_match = re.search(
            r"volume.*?(above|greater than|exceeds|higher than)\s+(\d+)\s*(million|thousand)?",
            text
        )
        if volume_match:
            vol = int(volume_match.group(2))
            unit = volume_match.group(3)

            if unit == "million":
                vol *= 1_000_000
            elif unit == "thousand":
                vol *= 1_000

            entry_rules.append(f"volume > {vol}")

        # ---------------- RSI ----------------
        rsi_match = re.search(
            r"rsi\s*(?:\((\d+)\))?.*?(below|less than|lower than)\s+(\d+)",
            text
        )
        if rsi_match:
            period = int(rsi_match.group(1)) if rsi_match.group(1) else 14
            threshold = int(rsi_match.group(3))
            exit_rules.append(f"rsi(close,{period}) < {threshold}")

        # ---------------- BUILD DSL ----------------
        dsl = ""

        if entry_rules:
            dsl += "ENTRY:\n"
            dsl += " AND ".join(entry_rules) + "\n\n"

        if exit_rules:
            dsl += "EXIT:\n"
            dsl += " AND ".join(exit_rules)

        return dsl
