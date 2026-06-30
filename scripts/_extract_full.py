#!/usr/bin/env python3
"""Extract full text from PDF using pdfplumber (better extraction)."""
import pdfplumber

pdf_path = "/Users/fabiotakwara/Documents/Imperveg/MARIANA-LOPES.pdf"
with pdfplumber.open(pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text() or ""
        print(f"\n===PAGE {i+1}===\n{text}")
