from os import environ
import openai
import numpy as np

openai.api_key = environ.get('OPENAPI_KEY')

def generate_embeddings(text, model='text-similarity-davinci-001'):
    text = text.replace('\n', '')
    embedding=  openai.embeddings.create(
        input=[text],
        model=model
    )

    return embedding.data[0].embedding

def similarity(embedding_a, embedding_b):
    return np.dot(embedding_a, embedding_b)

if __name__ == '__main__':
    
    i_a = 'That is a happy person'
    i_b = 'That is a sad person'

    em_a = generate_embeddings(i_a)
    em_b = generate_embeddings(i_b)

    print(similarity(em_a, em_b))

