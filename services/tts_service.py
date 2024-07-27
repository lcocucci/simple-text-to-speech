import datetime
import base64
import io
import wave
from gtts import gTTS
from pathlib import Path
from piper.voice import PiperVoice
from fastapi.responses import StreamingResponse
import os

# Configurar la ruta al modelo de Piper
model_path = Path("/usr/src/app/piper-models/es_MX-claude-high.onnx")
voice = PiperVoice.load(str(model_path))

# Asegurarse de que el directorio samples existe
os.makedirs("./samples", exist_ok=True)

# Síntesis de voz en local con Piper
async def synthesize_with_piper(text: str):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f'./samples/piper-sample-{now}.wav'
    
    with wave.open(file_path, "w") as wav_file:
        voice.synthesize(text, wav_file)
    
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    
    # Convertir a base64
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
    audio_buffer = io.BytesIO(base64.b64decode(audio_base64))
    
    return StreamingResponse(audio_buffer, media_type="audio/wav")

# Síntesis de voz utilizando gTTS
async def synthesize_with_gtts(text: str):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f'./samples/gtts-sample-{now}.mp3'
    
    tts = gTTS(text, lang='es', tld='us')
    tts.save(file_path)
    
    with open(file_path, "rb") as f:
        audio_bytes = f.read()
    
    # Convertir a base64
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
    audio_buffer = io.BytesIO(base64.b64decode(audio_base64))
    
    return StreamingResponse(audio_buffer, media_type="audio/mpeg")
