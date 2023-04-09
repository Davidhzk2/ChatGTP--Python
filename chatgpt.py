import openai

# Clave que se asocia a mi usuario
openai.api_key = "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"
# modulo openai y la clase Completion - operacion create 
# parametros habituales


while(True):

    prompt = input("\n Ingrese su pregunta: ")

    if prompt == "exit" or prompt == "close":
        break;

    completion = openai.Completion.create(engine="text-davinci-003",        #hace referncia al modelo entrenado 
                            prompt= prompt, #Pregunta que se le va realizar al gestor
                            n = 2,                                         #Numero de respuestas que recibimos
                            max_tokens=2048,                                #Maxima respuesta que nos va a dar admitiendo 4096
                            );

    print(completion.choices[0].text)
        
