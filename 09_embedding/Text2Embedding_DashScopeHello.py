# https://bailian.console.aliyun.com/cn-beijing/?productCode=p_efm&tab=doc#/doc/?type=model&url=2842587
import os

import dashscope
from http import HTTPStatus
from dotenv import load_dotenv
load_dotenv()
input_text = "衣服的质量杠杠的"

resp = dashscope.TextEmbedding.call(
    model="text-embedding-v4",
    input=input_text,
    api_key=os.getenv("DASHSCOPE_API_KEY")
)

if resp.status_code == HTTPStatus.OK:
    print(resp)


