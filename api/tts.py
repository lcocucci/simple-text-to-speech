from fastapi import APIRouter, HTTPException
from models.item import SynthesisRequest
from services.tts_service import synthesize_with_google_tts

router = APIRouter()

@router.post("/")
async def tts(request: SynthesisRequest):
    # if request.method == "local":
    #     audio = await synthesize_with_piper(request.text)
    if request.method == "api":
        audio = await synthesize_with_google_tts(request.text)
    else:
        raise HTTPException(status_code=400, detail="Invalid method")
    
    return {"audio": audio}