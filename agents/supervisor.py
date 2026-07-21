from agents.planner import PlannerAgent
from agents.search_agent import SearchAgent
from agents.paper_agent import PaperAgent
from agents.fact_checker import FactCheckerAgent
from agents.writer import WriterAgent


class SupervisorAgent:

    def __init__(self):

        self.planner = PlannerAgent()

        self.search = SearchAgent()

        self.paper = PaperAgent()

        self.fact_checker = FactCheckerAgent()

        self.writer = WriterAgent()

    def run(self, state):

        state = self.planner.run(state)

        state = self.search.run(state)

        state = self.paper.run(state)

        state = self.fact_checker.run(state)

        state = self.writer.run(state)

        return state