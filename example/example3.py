api = "bc5e51f6ce15640ba4da2002596d0909.x2oQXT6gCEbLtroJ"
from zhipuai import ZhipuAI


def chat(contents):
    client = ZhipuAI(api_key=api)  # 填写您自己的APIKey
    response = client.chat.completions.create(
        model="glm-4-flash",  # 填写需要调用的模型编码
        messages=[
            {"role": "user", "content": contents}
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    while True:
        i = input("请输入：")
        chat(i)