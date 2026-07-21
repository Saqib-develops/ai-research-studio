from agents.base_agent import BaseAgent
from services.groq_service import GroqService

SYSTEM_PROMPT = """
You are the Academic Paper Analysis Agent.

You will receive web search results.

Summarize them professionally.

Return:

1. Key Research Findings
2. Important Technologies
3. Current Trends
4. Challenges
5. Future Scope

Keep everything concise.
"""


class PaperAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Paper Agent",
            "One Shot"
        )

        self.llm = GroqService()

    def run(self, state):

        start = self.before_run(state)

        search_text = ""

        for item in state["search_results"]:

            search_text += f"""

========================================

TITLE

{item['title']}

SUMMARY

{item['body']}

SOURCE

{item['url']}

========================================
"""

        response = self.llm.generate_response(

            prompt=search_text,

            system_prompt=SYSTEM_PROMPT,

            temperature=0.3

        )

        state["papers"] = response

        self.after_run(state, start)

        return state