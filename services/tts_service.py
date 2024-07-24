from piper.voice import PiperVoice
from pathlib import Path
import base64
import io
import wave

# Define the path to the model
model_path = Path("/usr/src/app/piper-models/es_MX-claude-high.onnx")
voice = PiperVoice.load(str(model_path))

async def synthesize_with_piper(text: str) -> str:
    output_buffer = io.BytesIO()
    with wave.open(output_buffer, "w") as wav_file:
        voice.synthesize(text, wav_file)
    output_buffer.seek(0)
    audio_base64 = base64.b64encode(output_buffer.read()).decode("utf-8")
    return audio_base64
