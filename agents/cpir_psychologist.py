import os

class CPIRPsychologist:
    def __init__(self):
        # Load the CPIR Kernel Prompt
        prompt_path = os.path.join(os.path.dirname(__file__), '..', 'prompts', 'cpir_kernel.md')
        with open(prompt_path, 'r') as f:
            self.system_prompt = f.read()

    def analyze(self, system_description: str):
        """
        Simulates the LLM analysis for Insider Risk.
        """
        print("   🧠 [PSYCHOLOGIST] Profiling Human Factors...")
        
        # MOCK LOGIC:
        # Detects the "Triangle of Fraud" (Pressure/Debt + Opportunity/Override)
        if "debt" in system_description.lower() and "override" in system_description.lower():
            return {"status": "CRITICAL_RISK", "findings": "INSIDER THREAT: Operator under financial stress has direct override access."}
            
        return {"status": "SAFE", "findings": "No high-risk stressors detected."}
      
