import os
from dotenv import load_dotenv as ld

ld()


DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")
GOOGLE_API_KEY = os.getenv("API_KEY")
SEARCH_ENGINE_ID = os.getenv("SEARCH_ENGINE_ID")