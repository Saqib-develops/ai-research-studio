''' 
  This file handles all communication with the Groq api.
  pattern: oops

'''

from groq import Groq
from config import GROQ_API_KEY, MODEL, MAX_TOKENS

class GroqService:

    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate_response(
        self,
        prompt: str,
        temperature: float = 0.4,
        system_prompt: str = None
    ):

        messages = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        response = self.client.chat.completions.create(
            model=MODEL,
            messages=messages,
            temperature=temperature,
            max_tokens=int(MAX_TOKENS)
        )

        return response.choices[0].message.content