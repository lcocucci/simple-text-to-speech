from piper.voice import PiperVoice
from gtts import gTTS
from pathlib import Path
import base64
import wave
import io
import datetime

# Definimos el path en el que se encuentra el modelo de piper
model_path = Path("/usr/src/app/piper-models/es_MX-claude-high.onnx")
voice = PiperVoice.load(str(model_path))

# Sísntesis de voz en local con piper
async def synthesize_with_piper(text: str) -> str:
    output_buffer = io.BytesIO()
    with wave.open(output_buffer, "w") as wav_file:
        voice.synthesize(text, wav_file)
    output_buffer.seek(0)
    audio_base64 = base64.b64encode(output_buffer.read()).decode("utf-8")
    return audio_base64

# Síntesis de voz utilizando gTTS
async def synthesize_with_gtts(text: str) -> str:
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    tts = gTTS(text, lang='es', tld='us')
    tts.save(f'./samples/gtts-sample-{now}.mp3')
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    audio_base64 = base64.b64encode(audio_buffer.read()).decode("utf-8")
    return audio_base64