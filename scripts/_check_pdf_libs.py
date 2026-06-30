#!/usr/bin/env python3
"""Check PDF libraries available."""
import importlib
for mod_name in ['PyPDF2', 'PyPDF', 'pdfminer', 'pdfplumber', 'pdfminer.high_level', 'pikepdf', 'pdfminer.pdfinterp', 'pdfminer.converter', 'pdfminer.layout', 'pdftotext', 'pdfminer.pdfpage', 'pdfminer.utils']:
    try:
        importlib.import_module(mod_name)
        print(f'{mod_name}: available')
    except ImportError:
        pass
