import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from process import gen_ai_model

# Initialize FastAPI
app = FastAPI()
origins = ["*"]
methods = ["*"]
headers = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=methods,
    allow_headers=headers
)


@app.get("/")
async def ping():
    return "I am up and running"


@app.post("/chat")
async def chat(message):
    return gen_ai_model.chat(message)


if __name__ == "__main__":
    uvicorn.run(app, port=int(os.environ.get('PORT', 8080)), host="0.0.0.0")
