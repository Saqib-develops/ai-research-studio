from prompts.BasePrompt import BasePrompt

EXAMPLES = {

    "paper_agent": """
Example

Paper:
Transformers for NLP

Summary:
The paper introduces transformer architecture based on self-attention for sequence modelling.
"""
}


class OneShotPrompt(BasePrompt):

    def build(
        self,
        role: str,
        user_prompt: str,
        **kwargs
    ) -> str:

        example = EXAMPLES.get(role, "")

        return f"""
You are acting as the {role}.

Below is one example.

{example}

Now perform the same task.

Input:

{user_prompt}
"""