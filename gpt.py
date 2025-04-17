# from openai import OpenAI
# import os, dotenv
# dotenv.load_dotenv(dotenv_path='.env', override=True)

# client = OpenAI(
#   api_key=os.getenv("OPENAI_API_KEY"),
# )

# completion = client.chat.completions.create(
#   model="gpt-4o-mini",
#   store=True,
#   messages=[
#     {"role": "user", "content": "會講中文嗎?"}
#   ]
# )

# print(completion.choices[0].message)

import openai
from openai import OpenAI
import base64
import os, dotenv
dotenv.load_dotenv(dotenv_path='.env', override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 將圖片轉為 base64 URL 格式
def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# 圖片 base64 編碼
base64_image = encode_image_to_base64("./table.jpg")

# 將圖片封裝為 GPT 接受的 image_url 格式
image_message = {
    "type": "image_url",
    "image_url": {
        "url": f"data:image/jpeg;base64,{base64_image}"
    }
}

# 傳送訊息
completion = client.chat.completions.create(
    model="gpt-4o",  # 注意要用支援 vision 的模型（gpt-4o or gpt-4-vision-preview）
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "這張圖裡有什麼？"},
                image_message
            ]
        }
    ]
)

print("🧠 GPT 回答：", completion.choices[0].message.content)
