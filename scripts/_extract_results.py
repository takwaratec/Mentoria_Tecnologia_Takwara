#!/usr/bin/env python3
"""Extract results section from PDF."""
import PyPDF2

pdf_path = "/Users/fabiotakwara/Documents/Imperveg/MARIANA-LOPES.pdf"
reader = PyPDF2.PdfReader(pdf_path)
text = ""
for i, page in enumerate(reader.pages):
    text += f"\n===PAGE {i+1}===\n" + page.extract_text()

# Find results section
idx = text.find("CAPÍTULO 4:")
if idx >= 0:
    print(text[idx:])
else:
    # Print last 30 pages
    pages = text.split("===PAGE ")
    for p in pages[-30:]:
        print(p)
