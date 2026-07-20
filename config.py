'''this file loads the environment variables from .env'''

from dotenv import load_dotenv
import os 

load_dotenv() 

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL_NAME")
MAX_TOKENS =os.getenv("MAX_TOKEN_ALLOWED")
TEMPERATURE = os.getenv("TEMPERATURE")

