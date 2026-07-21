from prompts.BasePrompt import BasePrompt

class ZeroShotPrompt(BasePrompt):

    def build(
        self,
        role: str,
        user_prompt: str,
        **kwargs
    ) -> str:

        return f"""
You are acting as the {role} in an AI Research Multi-Agent System.

Your responsibility is ONLY the work assigned to the {role}.

User Query:
{user_prompt}

Instructions:
- Stay focused on your assigned role.
- Produce clear and concise output.
- Do not perform tasks belonging to other agents.
- Return only the requested result.
"""