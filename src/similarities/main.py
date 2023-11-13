from os import environ
import openai
import numpy as np

openai.api_key = environ.get('OPENAPI_KEY')

def generate_embeddings(text, model='text-similarity-davinci-001'):
    """
    Generates embeddings for the given text using the specified OpenAI model.

    Args:
    text (str): The input text to generate embeddings for.
    model (str): The OpenAI model to use for generating embeddings. Default is 'text-similarity-davinci-001'.

    Returns:
    numpy.ndarray: The embeddings generated for the input text.
    """
    text = text.replace('\n', '')
    embedding=  openai.embeddings.create(
        input=[text],
        model=model
    )

    return embedding.data[0].embedding


def similarity(embedding_a, embedding_b):
    """
    Calculates the cosine similarity between two embeddings.

    Args:
    embedding_a (numpy.ndarray): The first embedding.
    embedding_b (numpy.ndarray): The second embedding.

    Returns:
    float: The cosine similarity between the two embeddings.
    """
    return np.dot(embedding_a, embedding_b)

if __name__ == '__main__':
    
    i_a = 'That is a happy person'
    i_b = 'That is a sad person'

    em_a = generate_embeddings(i_a)
    em_b = generate_embeddings(i_b)

    print(similarity(em_a, em_b))

