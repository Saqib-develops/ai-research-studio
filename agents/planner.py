import json

from agents.base_agent import BaseAgent
from services.groq_service import GroqService


SYSTEM_PROMPT = """
You are the Planner Agent.

Analyze the user's research request.

Return ONLY valid JSON.

Example:

{
"title":"Quantum Computing",

"keywords":[
"Quantum Computing",
"Qubits",
"Quantum Algorithms",
"IBM Quantum",
"Google Quantum AI"
],

"tasks":[
"Understand fundamentals",
"Collect latest information",
"Analyze important developments",
"Verify technical claims",
"Generate professional report"
]
}

Rules

Return valid JSON only.

No markdown.

No explanation.

Keywords should be proper nouns or search terms.

Avoid sentences.
"""


class PlannerAgent(BaseAgent):

    def __init__(self):

        super().__init__(
            "Planner",
            "Zero Shot"
        )

        self.llm = GroqService()

    def run(self, state):

        start = self.before_run(state)

        response = self.llm.generate_response(

            prompt=state["query"],

            system_prompt=SYSTEM_PROMPT,

            temperature=0.2

        )

        try:

            cleaned = response.replace("```json", "").replace("```", "").strip()

            plan = json.loads(cleaned)

            state["plan"] = plan.get("tasks", [])

            state["keywords"] = plan.get("keywords", [])

        except Exception as e:

            print(e)

            state["plan"] = [
                "Understand the topic",
                "Collect information",
                "Analyze findings",
                "Verify claims",
                "Generate report"
            ]

            state["keywords"] = [
                state["query"]
            ]

        return state