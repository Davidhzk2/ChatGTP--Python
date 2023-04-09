import os 
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def createText():
    while(True):

        prompt = input("\n Ingrese su pregunta: ")

        if prompt == "exit" or prompt == "close":
            break;

        completion = openai.Completion.create(engine="text-davinci-003",  
                                prompt= prompt, 
                                n = 2,                                         
                                max_tokens=2048,                                 
                                );

        print(completion.choices[0].text)

def createImg():

    prompt = input("\n Ingrese text para crear una imagen: ")

    image = openai.Image.create(prompt= prompt);

    print(image.choices)


# ejecucion
entrada = input("\n Querieres  consultar una imagen o un texto ?: TEXT(1) IMAGE(2)")

if entrada == "1":
    createText()
elif entrada == "2":
    createImg()
else:
    print("No Podemos hacer nada, tu ingresaste \n"+ entrada)

    


     
