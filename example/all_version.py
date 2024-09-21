from importlib.metadata import version
print("all of version:")

print("tqdm version:   \t", version("tqdm"))
print("torch version:  \t", version("torch"))
print("zhipuai version:\t", version("zhipuai"))
print("fastapi version:\t", version("fastapi"))
print("uvicorn version:\t", version("uvicorn"))
print("pydantic version:\t", version("pydantic"))