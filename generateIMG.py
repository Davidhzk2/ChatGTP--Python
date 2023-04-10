import os 
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


while True:

    try:
        prompt = input("\n Ingrese texto para crear una imagen: ")

        if prompt == "exit":
            break

        response = openai.Image.create(prompt = prompt,
                                    n=3,
                                    response_format = "url");
        # print(image.data[0 + "\n" + image.data)
        print(response)
        # print(image.data)
        # print(response.data[0])

    except NameError :
        print("Something went wrong")
        





    


     
