from agents.supervisor import SupervisorAgent


class ResearchWorkflow:

    def __init__(self):
        self.supervisor = SupervisorAgent()

    def run(self, state):
        return self.supervisor.run(state)