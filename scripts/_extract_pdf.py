#!/usr/bin/env python3
"""Extract text from PDF using PyMuPDF."""
import fitz
import sys

doc = fitz.open(sys.argv[1])
print(f"Total pages: {len(doc)}")
for i, page in enumerate(doc):
    text = page.get_text()
    print(f"--- PAGE {i+1} ---")
    print(text)
