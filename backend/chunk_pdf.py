from langchain_text_splitters import RecursiveCharacterTextSplitter
from read_pdf import extract_text

pdf_path = "uploads/A2_Computer Science and Engineering_1.pdf"

text = extract_text(pdf_path)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_text(text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:5], start=1):
    print(f"\n===== Chunk {i} =====\n")
    print(chunk)