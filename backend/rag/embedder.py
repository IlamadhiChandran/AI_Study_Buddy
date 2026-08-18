from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient
import uuid

# Load embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("study_material")


def store_embeddings(chunks, source):
    """
    Converts chunks into embeddings and stores them in ChromaDB.
    """

    embeddings = model.encode(chunks).tolist()

    ids = [str(uuid.uuid4()) for _ in chunks]

    metadatas = [
        {"source": source}
        for _ in chunks
    ]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )

    return len(chunks)