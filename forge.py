from .agents.stpa_engineer import STPAEngineer
from .agents.cpir_psychologist import CPIRPsychologist
from .agents.physicist import Physicist

class AnvilForge:
    def __init__(self):
        self.engineer = STPAEngineer()
        self.psychologist = CPIRPsychologist()
        self.physicist = Physicist()

    def hammer_system(self, system_description: str):
        """
        Runs the system description through all 3 lenses in parallel.
        """
        print("\n🔨 ANVIL: Initializing Safety Audit...")
        print(f"Target System Snippet: {system_description[:50]}...\n")

        # 1. Parallel Execution
        # (In a real app, use asyncio.gather for speed)
        stpa_report = self.engineer.analyze(system_description)
        cpir_report = self.psychologist.analyze(system_description)
        t1_report = self.physicist.verify(system_description)

        # 2. Synthesis Logic
        # Priority 1: Physics (If it's impossible, nothing else matters)
        if t1_report["status"] == "IMPOSSIBLE":
            return {
                "status": "REJECTED (PHYSICS)",
                "critical_finding": t1_report["findings"]
            }

        # Priority 2: Human/Process Risk
        if cpir_report["status"] == "CRITICAL_RISK":
            return {
                "status": "REJECTED (HUMAN FACTORS)",
                "critical_finding": cpir_report["findings"],
                "engineering_note": stpa_report["findings"]
            }

        if stpa_report["status"] == "RISK":
            return {
                "status": "FLAGGED (ENGINEERING)",
                "critical_finding": stpa_report["findings"]
            }

        return {"status": "APPROVED", "details": "All agents passed."}
