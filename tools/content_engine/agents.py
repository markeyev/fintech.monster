from prompts import (
    JOURNALIST_SYSTEM_PROMPT,
    FACT_CHECKER_SYSTEM_PROMPT,
    LEGAL_REVIEWER_SYSTEM_PROMPT,
    EDITOR_SYSTEM_PROMPT,
    SEO_SPECIALIST_SYSTEM_PROMPT
)

import json

class DummyLLMClient:
    """
    Mock LLM client to simulate agent behavior until the SDK is integrated.
    """
    def generate(self, system_prompt, user_input):
        # Simulated responses for different personas
        if "Journalist" in system_prompt:
            return f"# NEWS: {user_input.get('title', 'Market Alert')}\n\nAutomated draft based on Harari-Pelevin style. It explores the systemic implications of the latest fintech development with a hint of dry irony."
        elif "Fact-Checker" in system_prompt:
            return "FACT REPORT:\n- Claim: 'Startup raised $100M' -> VERIFIED via Press Release (100% confidence)\n- Claim: 'Lead investor is Sequoia' -> UNVERIFIED (0% confidence - Source needed)"
        elif "Legal" in system_prompt:
            return "LEGAL REVIEW:\n- Confidence Check: Fact-checker score for lead investor is 0%. RECOMMENDED ACTION: Remove lead investor name until verified.\n- Compliance: Added standard financial advice disclaimer.\n- STATUS: [FINE TO PUBLISH IF EDITED]"
        elif "Editor" in system_prompt:
            return f"EDITORIAL REVISION:\n[Cleaned up news post with improved transitions and institutional tone.]\n\n- Removed unverified investor info.\n- Tightened the lead paragraph."
        elif "SEO" in system_prompt:
            return f"SEO OPTIMIZED POST:\n\nTitle: The Systemic Shift in Fintech Funding\nSlug: fintech-funding-systemic-shift\nTags: fintech, startups, investment\n\n[Full post content with keywords integrated.]"
        return "Simulated LLM response."

class Persona:
    def __init__(self, name, system_prompt):
        self.name = name
        self.system_prompt = system_prompt
        self.llm = DummyLLMClient()

    def process(self, context):
        print(f"[{self.name}] Processing...")
        return self.llm.generate(self.system_prompt, context)

class Journalist(Persona):
    def __init__(self):
        super().__init__("Journalist", JOURNALIST_SYSTEM_PROMPT)

class FactChecker(Persona):
    def __init__(self):
        super().__init__("Fact-Checker", FACT_CHECKER_SYSTEM_PROMPT)

class LegalReviewer(Persona):
    def __init__(self):
        super().__init__("Legal Reviewer", LEGAL_REVIEWER_SYSTEM_PROMPT)

class Editor(Persona):
    def __init__(self):
        super().__init__("Editor", EDITOR_SYSTEM_PROMPT)

class SEOSpecialist(Persona):
    def __init__(self):
        super().__init__("SEO Specialist", SEO_SPECIALIST_SYSTEM_PROMPT)
