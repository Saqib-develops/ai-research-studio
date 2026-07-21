from prompts.prompt_registry import PROMPT_REGISTRY


class PromptEngine:

    @staticmethod
    def build(
        strategy: str,
        role: str,
        user_prompt: str,
        **kwargs
    ):

        prompt_class = PROMPT_REGISTRY[strategy]

        return prompt_class().build(
            role=role,
            user_prompt=user_prompt,
            **kwargs
        )