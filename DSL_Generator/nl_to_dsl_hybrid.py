from DSL_Generator.nl_to_dsl import NLToDSLConverter1
from DSL_Generator.nl_to_dsl_llm import NLToDSLConverterLLM2

class NLToDSLHybrid:
    def __init__(self):
        self.regex_converter = NLToDSLConverter1()
        self.llm_converter = NLToDSLConverterLLM2()


    def _is_valid_dsl(self, dsl: str) -> bool:
        if not dsl:
            return False
        if "ENTRY:" not in dsl:
            return False
        if "EXIT:" not in dsl:
            return False
        return True
    
    
    def convert(self, text: str) -> str:
        # Step 1: Try regex
        dsl = self.regex_converter.convert(text)

        # Step 2: Validate regex output
        if self._is_valid_dsl(dsl):
            print("✔ Used REGEX parser")
            return dsl

        # Step 3: Fallback to LLM
        print("⚠ Regex failed → Trying Using LLM")
        return self.llm_converter.convert(text)

   
