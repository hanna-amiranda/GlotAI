import sys
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface
from glotai.config import API_KEY, IDIOMAS

def main():
    idioma = sys.argv[1] if len(sys.argv) > 1 else "ingles"
    if idioma not in IDIOMAS:
        print(f"Idioma no disponible. Opciones: {list(IDIOMAS)}")
        return

    client = ElevenLabs(api_key=API_KEY)
    conversation = Conversation(
        client,
        IDIOMAS[idioma]["agent_id"],
        requires_auth=True,
        audio_interface=DefaultAudioInterface(),
        callback_agent_response=lambda r: print(f"Tutor: {r}"),
        callback_user_transcript=lambda t: print(f"Tú: {t}"),
    )

    conversation.start_session()
    input("Presiona Enter para terminar...\n")
    conversation.end_session()

if __name__ == "__main__":
    main()