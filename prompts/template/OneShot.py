from prompts.BasePrompt import BasePrompt

class OneShotPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        prompt_template = f"""
        Example:
        Question:
        Explain Linear Search in Java.

        Answer:
        Linear Search checks each element one by one until the target is found.

        Now answer:

        {user_prompt}
        """
        return prompt_template