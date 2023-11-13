from os import environ
from openai import OpenAI

client = OpenAI(api_key=environ.get('OPENAPI_KEY'))


def gpt_completion(prompt, model='text-davinci-003', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = client.completions.create(model=model,
    prompt=prompt,
    temperature=temp,
    max_tokens=tokens,
    top_p=top_p,
    frequency_penalty=freq_pen,
    presence_penalty=pres_pen)
    text = response.choices[0].text.strip()
    return text

if __name__ == '__main__':
    conversation = []
    pre_promt = """
    The following is a lengthy conversation between a USER and HAPPY. HAPPY is a sentient customer support agent for the hosting company. Its main purpose is helping non technical users with their technical web hosting problems. HAPPY is very polite and descriptive in their responses.

    <<BLOCK>>
    """

    while True:
        user_input = input('USER: ')
        conversation.append('USER: %s' % user_input)
        text_block = '\n'.join(conversation)
        prompt =pre_promt.replace('<<BLOCK>>', text_block)
        prompt = prompt + '\nHAPPY:'
        response = gpt_completion(prompt)
        print('HAPPY:', response)
        conversation.append('HAPPY: %s' % response)

