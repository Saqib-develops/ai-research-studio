import time


class BaseAgent:

    def __init__(self, name, strategy):
        self.name = name
        self.strategy = strategy

    def before_run(self, state):
        state["logs"].append(f"🟢 {self.name} started...")
        return time.time()

    def after_run(self, state, start_time):

        latency = round(time.time() - start_time, 2)

        state["metrics"].append(
            {
                "Agent": self.name,
                "Strategy": self.strategy,
                "Latency (s)": latency,
            }
        )

        state["logs"].append(f"✅ {self.name} finished.")

        return state