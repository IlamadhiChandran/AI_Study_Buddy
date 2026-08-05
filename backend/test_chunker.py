from rag.reader import extract_text
from rag.chunker import chunk_text

text = extract_text("uploads/A2_Computer Science and Engineering_1.pdf")

chunks = chunk_text(text)

print("Total Chunks:", len(chunks))

print("\n===== First Chunk =====\n")
print(chunks[0])