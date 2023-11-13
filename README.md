# GTP Playground

## Getting started

make a venv `python -m venv .venv`
Activate the venv `source .venv/bin/activate`
install the requirements `pip install -r requirements.txt`
`cp example.env .env` and add your openapi key

Example use cases

- `./src/chatbot` is an example assistant using the chat completions API
- `./src/completions` is an example of creating a chatbot using the old completion API
- `./src/similarities` is an example of using embeddings to do text similarity

## Notes and links

Guide to embeddings https://platform.openai.com/docs/guides/embeddings

The new text-embedding-ada-002 model is not outperforming text-similarity-davinci-001 on the SentEval linear probing classification benchmark. For tasks that require training a light-weighted linear layer on top of embedding vectors for classification prediction, we suggest comparing the new model to text-similarity-davinci-001 and choosing whichever model gives optimal performance.