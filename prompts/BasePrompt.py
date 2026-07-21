from abc import ABC, abstractmethod


class BasePrompt(ABC):

    @abstractmethod
    def build(
        self,
        role: str,
        user_prompt: str,
        **kwargs
    ) -> str:
        """
        Build the final prompt for an AI agent.

        Parameters:
        ----------
        role : str
            The agent role (planner, search_agent, writer, etc.)

        user_prompt : str
            The user's original research query.

        **kwargs :
            Additional information like examples, context,
            search results, papers, etc.

        Returns:
        -------
        str
            Final prompt sent to the LLM.
        """
        pass