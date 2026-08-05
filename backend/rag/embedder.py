from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient

# Load embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("study_material")


def store_embeddings(chunks):
    """
    Converts chunks into embeddings and stores them in ChromaDB.
    """

    embeddings = model.encode(chunks).tolist()

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"chunk_{i}" for i in range(len(chunks))]
    )

    return len(chunks)