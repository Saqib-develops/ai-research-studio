from agents.base_agent import BaseAgent
from services.search_service import SearchService


class SearchAgent(BaseAgent):

    def __init__(self):

        super().__init__(

            "Research Agent",

            "Zero Shot"

        )

        self.search = SearchService()

    def run(self, state):

        start = self.before_run(state)

        all_results = []

        for keyword in state["keywords"]:

            result = self.search.search(keyword)

            if result:

                all_results.append(result)

        if len(all_results) == 0:

            result = self.search.search(state["query"])

            if result:

                all_results.append(result)

        state["search_results"] = all_results

        self.after_run(state, start)

        return state