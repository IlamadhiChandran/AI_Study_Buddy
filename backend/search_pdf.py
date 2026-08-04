from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Connect to ChromaDB
client = PersistentClient(path="./chroma_db")

collection = client.get_collection("study_material")

# Ask the user a question
query = input("Ask a question: ")

# Convert question to embedding
query_embedding = model.encode(query).tolist()

# Search ChromaDB
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

print("\n========== SEARCH RESULTS ==========\n")

for i, document in enumerate(results["documents"][0], start=1):
    print(f"Result {i}")
    print("-" * 50)
    print(document)
    print()