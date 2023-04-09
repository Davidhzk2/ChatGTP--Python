import openai

openai.api_key = "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"

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
        
