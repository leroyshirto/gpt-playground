from os import environ
from openai import OpenAI

client = OpenAI(api_key=environ.get('OPENAPI_KEY'))


def get_chat_completion(messages, model='gpt-4-1106-preview'):
    response = client.chat.completions.create(
        messages=messages,
        model=model,
    )
    text = response.choices[0].message.content.strip()
    return text

if __name__ == '__main__':
    system_message = "The following is a lengthy conversation between a USER and HAPPY. HAPPY is a sentient customer support agent for the hosting company. Its main purpose is helping non technical users with their technical web hosting problems. HAPPY is very polite and descriptive in their responses."
    conversation = [
        {
            "role": "system",
            "content": system_message
        }
    ]

    try:
        while True:
            user_input = input('USER: ')

            prompt = user_input.encode(encoding='ASCII',errors='ignore').decode()
            conversation.append(
                {
                    "role": "system",
                    "content": prompt
                }
            )

            response = get_chat_completion(messages=conversation)
            print('🤖 HAPPY:', response)
            conversation.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )
            print("")
    except KeyboardInterrupt:
        print('Goodbye!')

