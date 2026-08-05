from rag.reader import extract_text

text = extract_text("uploads/A2_Computer Science and Engineering_1.pdf")

print(text[:1000])