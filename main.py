from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from models.item import SynthesisRequest
from services.tts_service import synthesize_with_piper
import base64
import io

app = FastAPI()

@app.post("/synthesize")
async def synthesize(request: SynthesisRequest):
    if request.method == "local":
        audio = await synthesize_with_piper(request.text)
    else:
        raise HTTPException(status_code=400, detail="Invalid method")
    
    audio_buffer = io.BytesIO(base64.b64decode(audio))
    return StreamingResponse(audio_buffer, media_type="audio/mp3")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Text-to-Speech API"}
