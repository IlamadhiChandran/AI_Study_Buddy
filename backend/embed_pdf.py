from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient

from chunk_pdf import chunks

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create Chroma database
client = PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="study_material"
)

# Convert chunks into embeddings
embeddings = model.encode(chunks).tolist()

# Store embeddings in ChromaDB
for i, chunk in enumerate(chunks):
    collection.add(
        ids=[str(i)],
        embeddings=[embeddings[i]],
        documents=[chunk]
    )

print(f"\n✅ Stored {len(chunks)} chunks in ChromaDB")