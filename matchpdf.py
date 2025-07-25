import fitz  

def extract_text(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def compare_pdfs(pdf_path1, pdf_path2):
    text1 = extract_text(pdf_path1)
    text2 = extract_text(pdf_path2)
    if text1 == text2:
        return True
    else:
        return False

pdf1 = "file1.pdf"
pdf2 = "file2.pdf"
if compare_pdfs(pdf1, pdf2):
    print("The PDFs have the same text content.")
else:
    print("The PDFs have different text content.")
