from google.cloud import texttospeech
# import piper
import base64

# model_path = "path/to/piper/model"
# voice = piper.Voice(model_path)

# async def synthesize_with_piper(text: str) -> str:
#     audio = voice.synthesize(text)
#     audio_base64 = base64.b64encode(audio).decode("utf-8")
#     return audio_base64


async def synthesize_with_google_tts(text: str) -> str:
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )
    audio_base64 = base64.b64encode(response.audio_content).decode("utf-8")
    return audio_base64