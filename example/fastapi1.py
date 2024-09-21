# main.py
from fastapi import FastAPI
from example3 import chat

app = FastAPI()

@app.get("/")
async def read_root():
    name = chat("我是你爹")
    return {"message": name}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi1:app", host="127.0.0.1", port=8000, reload=True)

