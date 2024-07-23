from fastapi import FastAPI, HTTPException
# from api.tts import tts
from services.tts_service import synthesize_with_google_tts 
from models.item import SynthesisRequest

app = FastAPI()

@app.get('/')
async def root():
    return {'greetings': 'welcome to the FastAPI app'}


@app.post("/tts")
async def tts(request: SynthesisRequest):
    # if request.method == "local":
    #     audio = await synthesize_with_piper(request.text)
    if request.method == "api":
        audio = await synthesize_with_google_tts(request.text)
    else:
        raise HTTPException(status_code=400, detail="Invalid method")
    
    return {"audio": audio}