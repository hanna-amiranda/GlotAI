import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ELEVENLABS_API_KEY")

IDIOMAS = {
    "ingles": {"nombre": "English", "agent_id": os.getenv("AGENT_ID_INGLES")},
    "italiano": {"nombre": "Italiano", "agent_id": os.getenv("AGENT_ID_ITALIANO")},
}