from pydantic import BaseModel

class SynthesisRequest(BaseModel):
    text: str
    method: str  # 'local' para Piper, 'api' para Google TTS
