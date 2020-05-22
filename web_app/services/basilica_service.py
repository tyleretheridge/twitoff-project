# web_app/services/basilica_service.py

import os
from dotenv import load_dotenv
from basilica import Connection

load_dotenv()
BASILICA_API_KEY = os.getenv("BASILICA_API_KEY", default="OOPS")

# Create connection to Basilica API object
connection = Connection(BASILICA_API_KEY)
print(type(connection))


if __name__ == "__main__":

    embedding = connection.embed_sentence("HELLO WORLD")
    print(embedding)

    sentences = [
        "This is a sentence!",
        "This is a similar sentence!",
        "I don't think this sentence is very similar at all...",
    ]

    embeddings = list(connection.embed_sentences(sentences))
    for embed in embeddings:
        print("----------")
        # a list with 768 floats from -1 to 1
        print(embed)
