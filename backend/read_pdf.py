import fitz


def extract_text(pdf_path):
    doc = fitz.open(pdf_path)

    text = ""

    print(f"Number of pages: {len(doc)}")

    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        page_text = page.get_text()

        print(f"\n----- Page {page_number + 1} -----\n")

        text += page_text

    doc.close()

    return text


if __name__ == "__main__":
    pdf_path = "uploads/A2_Computer Science and Engineering_1.pdf"

    text = extract_text(pdf_path)

    print(text)