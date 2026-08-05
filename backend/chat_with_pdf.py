import os

from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer
from chromadb import PersistentClient

# Load API key
print("1. Loading environment...")
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
print("2. API key loaded")

client = genai.Client(api_key=api_key)
print("3. Gemini client created")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
print("4. Embedding model loaded")

db = PersistentClient(path="./chroma_db")
print("5. ChromaDB connected")

collection = db.get_collection("study_material")
print("6. Collection loaded")

question = input("Ask a question: ")
print("7. Question received")

# Convert question into an embedding
query_embedding = embedding_model.encode(question).tolist()

# Search the vector database
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

context = "\n\n".join(results["documents"][0])

print("\n===== Retrieved Context =====\n")
print(context)
print("\n=============================\n")

prompt = f"""
You are an AI Study Buddy.

Answer ONLY using the context below.

If the answer cannot be found in the context, reply exactly:

I couldn't find that information in the uploaded PDF.

Context:
{context}

Question:
{question}
"""

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
)

print("\n========== AI ANSWER ==========\n")
print(response.text)