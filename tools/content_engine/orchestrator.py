from agents import Journalist, FactChecker, LegalReviewer, Editor, SEOSpecialist
from verification import VerificationManager

class ContentOrchestrator:
    def __init__(self):
        self.journalist = Journalist()
        self.fact_checker = FactChecker()
        self.legal_reviewer = LegalReviewer()
        self.editor = Editor()
        self.seo = SEOSpecialist()
        self.verifier = VerificationManager()

    def run_pipeline(self, initial_info):
        # 1. Topic Evaluation & Drafting
        draft = self.journalist.process(initial_info)
        
        # 2. Fact Checking
        fact_report = self.fact_checker.process(draft)
        
        # 3. Legal Review
        legal_report = self.legal_reviewer.process({"draft": draft, "facts": fact_report})
        
        # Human-in-the-loop: Verification after Legal/Fact Check
        approved, draft = self.verifier.request_approval("Legal & Fact Check", f"FACT REPORT:\n{fact_report}\n\nLEGAL REPORT:\n{legal_report}\n\nDRAFT:\n{draft}")
        if not approved:
            print("Pipeline rejected by user at Legal/Fact Check stage.")
            return None

        # 4. Editing
        edited_post = self.editor.process(draft)
        
        # Human-in-the-loop: Verification after Editing
        approved, edited_post = self.verifier.request_approval("Editorial Review", edited_post)
        if not approved:
            print("Pipeline rejected by user at Editorial stage.")
            return None

        # 5. SEO Optimization
        final_post = self.seo.process(edited_post)
        
        # Final Human-in-the-loop: Final Polish
        approved, final_post = self.verifier.request_approval("Final SEO & Readability Review", final_post)
        if not approved:
            print("Pipeline rejected by user at final stage.")
            return None
            
        return final_post
