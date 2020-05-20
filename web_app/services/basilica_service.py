# web_app/services/basilica_service.py

from dotenv import load_dotenv
import os
import basilica

load_dotenv()
BASILICA_API_KEY = os.getenv("BASILICA_API_KEY")

sentences = [
    "This is a sentence!",
    "This is a similar sentence!",
    "I don't think this sentence is very similar at all...",
]
connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection))

embeddings = list(connection.embed_sentences(sentences))
print(embeddings)
