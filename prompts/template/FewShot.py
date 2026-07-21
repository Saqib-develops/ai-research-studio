from prompts.BasePrompt import BasePrompt

class FewShotPrompt(BasePrompt):

    def build(self, user_prompt: str) -> str:
        prompt_template = f"""

        Question:
        Explain Array.

        Answer:
        An Array stores elements of the same data type.

        --------------------------------

        Example 2

        Question:
        Explain Linear Search.

        Answer:
        Linear Search checks every element sequentially.

        --------------------------------

        Example 3

        Question:
        Explain Bubble Sort.

        Answer:
        Bubble Sort repeatedly swaps adjacent elements.

        --------------------------------

        Now answer:

        {user_prompt}
        """
        return prompt_template