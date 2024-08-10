import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import translation

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return "Hello world"

# ?source=english&target=spanish&text=hello
@app.get("/translate")
def translate(source: str, target: str, text: str):
    translated_text = translation.translate(source, target, text)
    return {"translation": translated_text}

if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 8000

    uvicorn.run(app, host=HOST, port=PORT)