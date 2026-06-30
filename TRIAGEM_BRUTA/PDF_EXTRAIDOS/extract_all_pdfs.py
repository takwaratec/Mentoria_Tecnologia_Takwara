#!/usr/bin/env python3
"""
Extract ALL PDFs from IFB Bibliografia Consultada directory to .md text files using PyMuPDF.
Scans root + subdirectories recursively.
"""

import os
import re
import sys
import fitz  # PyMuPDF

# Paths
PDF_BASE = "/Users/fabiotakwara/Documents/IFB Relatorio Final/Bibliografia Consultada"
OUTPUT_BASE = "/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara/TRIAGEM_BRUTA/PDF_EXTRAIDOS"

def sanitize_filename(name):
    """Remove/replace special chars for clean filenames."""
    # Remove .pdf extension first
    name = re.sub(r'\.pdf$', '', name, flags=re.IGNORECASE)
    # Replace spaces and special chars
    name = name.replace(' ', '_')
    name = name.replace(',', '')
    name = name.replace('(', '')
    name = name.replace(')', '')
    name = name.replace('[', '')
    name = name.replace(']', '')
    name = name.replace('{', '')
    name = name.replace('}', '')
    name = name.replace("'", '')
    name = name.replace('"', '')
    name = name.replace('!', '')
    name = name.replace('?', '')
    name = name.replace(':', '')
    name = name.replace(';', '')
    name = name.replace('/', '-')
    name = name.replace('\\', '-')
    # Collapse multiple underscores
    name = re.sub(r'_+', '_', name)
    # Remove leading/trailing underscores
    name = name.strip('_')
    return name

def get_relative_subdir(pdf_full_path):
    """Get the subdirectory path relative to PDF_BASE."""
    rel = os.path.relpath(pdf_full_path, PDF_BASE)
    return os.path.dirname(rel)

results = {
    'extracted': [],
    'empty_scanned': [],
    'errors': [],
    'total': 0
}

# Walk through all directories recursively
for root, dirs, files in os.walk(PDF_BASE):
    # Skip hidden dirs
    dirs[:] = [d for d in dirs if not d.startswith('.')]
    
    for fname in sorted(files):
        if not fname.lower().endswith('.pdf'):
            continue
        
        pdf_path = os.path.join(root, fname)
        results['total'] += 1
        
        # Determine output path preserving subdirectory structure
        rel_subdir = get_relative_subdir(pdf_path)
        if rel_subdir:
            out_subdir = os.path.join(OUTPUT_BASE, rel_subdir)
        else:
            out_subdir = OUTPUT_BASE
        os.makedirs(out_subdir, exist_ok=True)
        
        # Create sanitized output name
        base = sanitize_filename(fname)
        out_name = base + '.md'
        out_path = os.path.join(out_subdir, out_name)
        
        # File size
        fsize = os.path.getsize(pdf_path)
        
        print(f"[{results['total']:3d}] Processing: {fname}")
        print(f"      Size: {fsize/1024:.1f} KB, Output: {out_name}")
        
        try:
            doc = fitz.open(pdf_path)
            text_parts = []
            page_count = doc.page_count
            
            for page_num in range(page_count):
                page = doc.load_page(page_num)
                page_text = page.get_text()
                text_parts.append(page_text)
            
            full_text = '\n'.join(text_parts)
            doc.close()
            
            # Write to file
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(full_text)
            
            # Check if it's empty (likely scanned)
            text_len = len(full_text.strip())
            if text_len < 50:  # Very little text extracted = scanned/image PDF
                results['empty_scanned'].append({
                    'path': pdf_path,
                    'file': fname,
                    'size_kb': round(fsize/1024, 1),
                    'pages': page_count,
                    'chars': text_len,
                    'output': out_name
                })
                status = "SCANNED/IMAGE-ONLY"
            else:
                results['extracted'].append({
                    'path': pdf_path,
                    'file': fname,
                    'size_kb': round(fsize/1024, 1),
                    'pages': page_count,
                    'chars': text_len,
                    'output': out_name
                })
                status = "TEXT EXTRACTED"
            
            print(f"      Status: {status} ({page_count} pages, {text_len} chars)")
            
        except Exception as e:
            results['errors'].append({
                'path': pdf_path,
                'file': fname,
                'error': str(e)
            })
            print(f"      ERROR: {e}")
        
        print()

# Print summary
print("=" * 70)
print("EXTRACTION COMPLETE")
print("=" * 70)
print(f"Total PDFs processed: {results['total']}")
print(f"Text extracted OK:    {len(results['extracted'])}")
print(f"Scanned/image-only:   {len(results['empty_scanned'])}")
print(f"Errors:               {len(results['errors'])}")

if results['extracted']:
    print("\n--- EXTRACTED PDFs ---")
    for r in results['extracted']:
        print(f"  {r['output']} ({r['chars']} chars, {r['pages']} pages)")

if results['empty_scanned']:
    print("\n--- SCANNED/IMAGE-ONLY PDFs (little to no text) ---")
    for r in results['empty_scanned']:
        print(f"  {r['file']} ({r['size_kb']} KB, {r['pages']} pages, {r['chars']} chars extracted)")

if results['errors']:
    print("\n--- ERRORS ---")
    for r in results['errors']:
        print(f"  {r['file']}: {r['error']}")

print(f"\nOutput directory: {OUTPUT_BASE}")
