from prompts.BasePrompt import BasePrompt

EXAMPLES = {

    "fact_checker": """

Claim:
Python was released in 2015.

Result:
False

Reason:
Python was first released in 1991.

----------------------

Claim:
GPT stands for Generative Pretrained Transformer.

Result:
True

Reason:
This is the official expansion.
"""
}


class FewShotPrompt(BasePrompt):

    def build(
        self,
        role: str,
        user_prompt: str,
        **kwargs
    ) -> str:

        examples = EXAMPLES.get(role, "")

        return f"""
You are acting as the {role}.

Learn from these examples.

{examples}

Now evaluate:

{user_prompt}
"""