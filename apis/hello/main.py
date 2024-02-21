from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import argparse
from spai.storage import Storage
from spai.config import SPAIVars

app = FastAPI(title="analytics")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

storage = Storage()
data = storage["data"]
vars = SPAIVars()

@app.get("/")
async def hello():
    print("Hello, SPAI!")
    print("Files in storage", data.list())
    print("Variables", vars)
    return {"data": vars["some_data"]}

# need this to run in background
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="0.0.0.0")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    uvicorn.run(app, host=args.host, port=args.port)
