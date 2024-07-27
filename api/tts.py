from fastapi import APIRouter, HTTPException
from models.item import SynthesisRequest
from services.tts_service import synthesize_with_gtts, synthesize_with_piper

router = APIRouter()

@router.post("/tts")
async def tts(request: SynthesisRequest):
    if request.method == "api":
        return await synthesize_with_gtts(request.text)
    elif request.method == "local":
        return await synthesize_with_piper(request.text)
    else:
        raise HTTPException(status_code=400, detail="Invalid method")