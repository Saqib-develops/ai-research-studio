from agents.planner import PlannerAgent
from agents.search_agent import SearchAgent
from agents.paper_agent import PaperAgent
from agents.fact_checker import FactCheckerAgent
from agents.writer import WriterAgent


class SupervisorAgent:

    def __init__(self):

        self.pipeline = [

            PlannerAgent(),

            SearchAgent(),

            PaperAgent(),

            FactCheckerAgent(),

            WriterAgent()

        ]

    def run(self, state):

        for agent in self.pipeline:
            state = agent.run(state)

        return state