from gtts import gTTS
from google.cloud import texttospeech
import base64
import io
import datetime

# Google tts (basic synthesis)

async def synthesize_with_gtts(text: str) -> str:
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    tts = gTTS(text, lang='es', tld='us')
    tts.save(f'./samples/gtts-sample-{now}.mp3')
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    audio_base64 = base64.b64encode(audio_buffer.read()).decode("utf-8")
    return audio_base64


# Google Cloud tts (premium synthesis)

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