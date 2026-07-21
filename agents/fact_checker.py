from agents.base_agent import BaseAgent
from services.groq_service import GroqService


SYSTEM_PROMPT = """
You are the Fact Checker Agent.

Example

Claim:
Python was released in 2015.

Result:
False

Reason:
Python was released in 1991.

-------------------------

Claim:
GPT stands for Generative Pretrained Transformer.

Result:
True

-------------------------

Verify the given research.
"""


class FactCheckerAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Fact Checker",
            "Few Shot"
        )

        self.llm = GroqService()

    def run(self, state):

        start = self.before_run(state)

        response = self.llm.generate_response(

            prompt=state["papers"],

            system_prompt=SYSTEM_PROMPT,

            temperature=0.2

        )

        state["verified_data"] = response

        self.after_run(state, start)

        return state