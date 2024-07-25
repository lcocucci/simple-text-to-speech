from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
# from api.tts import tts
from services.tts_service import synthesize_with_google_tts, synthesize_with_gtts 
from models.item import SynthesisRequest
import base64
import io


app = FastAPI()

@app.get('/')
async def root():
    return {'greetings': 'welcome to the FastAPI app'}


@app.post("/tts")
async def tts(request: SynthesisRequest):
    if request.method == "api":
        audio = await synthesize_with_google_tts(request.text)
    elif request.method == "gtts":
        audio = await synthesize_with_gtts(request.text)
    else:
        raise HTTPException(status_code=400, detail="Invalid method")
    
    audio_buffer = io.BytesIO(base64.b64decode(audio))
    return StreamingResponse(audio_buffer, media_type="audio/mp3")
    
    return {"audio": audio}