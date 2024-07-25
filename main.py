from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
# from api.tts import tts
from services.tts_service import synthesize_with_google_tts, synthesize_with_gtts 
from models.item import SynthesisRequest
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
    
    return {"audio": audio}