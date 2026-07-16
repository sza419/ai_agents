import os

from dotenv import load_dotenv

from litellm import completion

load_dotenv()
full_history = []
def get_history(history):
    history_list = ''
    for messages in history:
        history_list += f'{messages["role"]} - {messages["content"]}\n'

    return history_list
        
        
    
def return_history(messages):
    return(messages)
system_prompt = f'''
Ты учебный помощник. Отвечай кратко и понятно
Ты возвращаешь только валидный JSON в ответе. 

'''
gigachat_credentials = os.getenv("GIGACHAT_CREDENTIALS")
def ask_question(question):
    response = completion(
        model = "ollama/qwen2.5-coder:7b",
        messages=[
            {
                "role": "system", 
                "content": system_prompt
            },
            {

                "role": "user",
                "content": get_history(full_history) + f'user - {question}'
            },

        ],
        ssl_verify=False,
    )


    answer = response.choices[0].message.content

    full_history.extend(
        [
            {

                "role":"user",
                "content": question
            },
            {
                "role": "system", 
                "content": answer
            }
        ]
    )
    return answer