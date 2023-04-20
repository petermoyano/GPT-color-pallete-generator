import openai
from dotenv import dotenv_values

config = dotenv_values()
openai.api_key = config["OPENAI_KEY"]

res = openai.Completion.create(
    model="text-davinci-003",
    prompt="Name a good son to code with:"
)
print(res)
