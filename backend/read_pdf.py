import fitz

pdf_path = "uploads/A2_Computer Science and Engineering_1.pdf"

doc = fitz.open(pdf_path)

print(f"Number of pages: {len(doc)}")

for page_number in range(len(doc)):
    page = doc.load_page(page_number)
    text = page.get_text()

    print(f"\n----- Page {page_number + 1} -----\n")
    print(text)