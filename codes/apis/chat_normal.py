from fastapi import APIRouter
from pydantic import BaseModel
from codes.chat_models.chat_glm import *

Chat = APIRouter()


class Message(BaseModel):
    message: str


class Response(BaseModel):
    response: str


@Chat.post("/chat", response_model=Response, summary="普通对话", description="这是与智谱清言聊天的入口")
async def chat(content: Message):
    response = chat_glm_normal(content.message)

    return Response(response=response)
