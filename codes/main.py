import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from codes.apis.chat_normal import Chat

app = FastAPI()

app.include_router(Chat, prefix="/chat", tags=["chat_api"])


@app.get("/", tags=["PS-GPT"], summary="主页", description="这是网站的主页。", status_code=200, name="index",
         responses={404: {"description": "没网"}}, response_description="主页内容", )
async def index():
    with open("templates/index.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    return HTMLResponse(content=html_content, status_code=200)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
