from PyPDF2 import PdfReader

file_path = "example.pdf"
reader = PdfReader(file_path)

if reader.is_encrypted:
    print("The PDF is encrypted. Decrypt it before proceeding.")
else:
    print("The PDF is safe to process.")
    
import fitz  # PyMuPDF

file_path = "example.pdf"
doc = fitz.open(file_path)

for page in doc:
    areas = page.search_for("Sensitive Info")
    for area in areas:
        page.add_redact_annot(area, fill=(0, 0, 0))  # Black out the text
        page.apply_redactions()

doc.save("redacted_example.pdf")

import pikepdf

file_path = "example.pdf"
with pikepdf.Pdf.open(file_path) as pdf:
    pdf.metadata.clear()
    pdf.save("cleaned_example.pdf")
