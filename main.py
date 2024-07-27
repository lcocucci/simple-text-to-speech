from fastapi import FastAPI
from api import tts


app = FastAPI()

app.include_router(tts.router, prefix='/api', tags=['tts'])

@app.get('/')
def root():
    return {'message': 'Welcome :)'}