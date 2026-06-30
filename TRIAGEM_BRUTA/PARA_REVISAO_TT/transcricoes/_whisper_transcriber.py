#!/usr/bin/env python3
import os, sys
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
from faster_whisper import WhisperModel

wav_path = sys.argv[1]
out_path = sys.argv[2]

model = WhisperModel('base', device='cpu', compute_type='int8')
segments, info = model.transcribe(wav_path, language='pt')
texts = []
for seg in segments:
    texts.append(f"[{seg.start:.1f}s - {seg.end:.1f}s] " + seg.text)
result = "\n".join(texts)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write("# Transcricao\n\n")
    f.write(result + "\n")

print(f"OK: {len(result)} chars -> {out_path}")
