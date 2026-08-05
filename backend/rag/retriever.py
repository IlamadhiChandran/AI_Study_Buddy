from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = PersistentClient(path="./chroma_db")
collection = client.get_collection("study_material")


def retrieve_context(question, n_results=3):
    """
    Retrieves the most relevant chunks for a question.
    """

    query_embedding = model.encode(question).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return "\n\n".join(results["documents"][0])