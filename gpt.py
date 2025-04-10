from openai import OpenAI
import os, dotenv
dotenv.load_dotenv(dotenv_path='.env', override=True)

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "會講中文嗎?"}
  ]
)

print(completion.choices[0].message)