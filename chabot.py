import openai

openai.api_key = "sk-"

def generate_chat_response(messages, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,    
            messages=messages  
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    messages = [
        {"role": "system", "content": "You are a helpful university assistant."},
        {"role": "user", "content": "Tell me programas Universidad Peruana de Ciencias Aplicadas has."}
    ]
    response = generate_chat_response(messages)
    print("AI Response:", response)
