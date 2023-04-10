import os 
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    prompt = input("\n Ingrese text para crear una imagen: ")
    image = openai.Image.create(prompt = prompt,
                                n=2,
                                response_format = "url");
    # print(image.data[0 + "\n" + image.data)
    # print(image)
    # print(image.data)
    print(image.data[0])

except NameError :
    print("Something went wrong")
    





    


     
