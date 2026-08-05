from rag.reader import extract_text
from rag.chunker import chunk_text
from rag.embedder import store_embeddings

text = extract_text("uploads/A2_Computer Science and Engineering_1.pdf")

chunks = chunk_text(text)

count = store_embeddings(chunks)

print(f"Stored {count} chunks successfully!")