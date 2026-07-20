''' 
  This file handles all communication with the Groq api.
  pattern: oops

'''

from groq import Groq
from config import GROQ_API_KEY, MODEL, MAX_TOKENS

class GroqService:
    def __init__(self):
        self.client = Groq(api_key=GROQ_API_KEY)

    def generate_response(self,prompt,temperate,role="user"):
        response = self.client.chat.completions.create(
            model = MODEL,
            messages= [
                {
                    "role" : role,
                    "content": prompt
                }
            ],
            max_tokens = int(MAX_TOKENS),
            temperature=float(temperate)
        )
        return response.choices[0].message.content
