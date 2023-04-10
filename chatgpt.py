import os 
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


while True:
    prompt = input("\n Ingrese su pregunta:")

    if prompt == "exit" or prompt == "close":
        break
    
    completion = openai.Completion.create(engine="text-davinci-003",
                    prompt = prompt,
                    max_tokens = 2048)

    print(completion.choices[0].text)