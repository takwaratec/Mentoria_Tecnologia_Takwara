#!/usr/bin/env python3
"""Transcrever todos os .m4a do Takwara-Tech/docs/audio/ e BAncadas/"""
import os, subprocess, sys, json, glob

WHISPER_ENV = "/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3"
OUT_DIR = "/Users/fabiotakwara/Documents/GitHub/Mentoria_Tecnologia_Takwara/TRIAGEM_BRUTA/PARA_REVISAO_TT/transcricoes"
TT_AUDIO = "/Users/fabiotakwara/Documents/GitHub/Takwara-Tech/docs/audio"
TT_BANCADAS = "/Users/fabiotakwara/Documents/GitHub/Takwara-Tech/docs/BAncadas"
os.makedirs(OUT_DIR, exist_ok=True)

def run(cmd, timeout=600):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout)
    return r.stdout.strip(), r.stderr.strip(), r.returncode

TRANSCRIBE_PY = os.path.join(OUT_DIR, "_whisper_transcriber.py")
with open(TRANSCRIBE_PY, 'w') as f:
    f.write('''#!/usr/bin/env python3
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
result = "\\n".join(texts)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write("# Transcricao\\n\\n")
    f.write(result + "\\n")

print(f"OK: {len(result)} chars -> {out_path}")
''')

import os as _os
_os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

def transcribe_one(m4a_path):
    base = os.path.splitext(os.path.basename(m4a_path))[0]
    safe = "".join(c if c.isalnum() or c in "._- " else "_" for c in base)
    out_md = os.path.join(OUT_DIR, f"{safe}.md")
    if os.path.exists(out_md):
        print(f"  Já existe: {safe}.md")
        return out_md

    wav = os.path.join(OUT_DIR, f"{safe}.wav")
    
    # Step 1: convert to wav 16kHz mono
    print(f"  Convertendo {base}...")
    out, err, code = run(f'ffmpeg -y -i "{m4a_path}" -ar 16000 -ac 1 "{wav}" 2>&1')
    if code != 0 or not os.path.exists(wav):
        print(f"  ERRO conversao: {base}: {err[:200]}")
        return None
    
    wav_size = os.path.getsize(wav)
    print(f"  WAV: {wav_size//1024}KB")
    
    # Step 2: transcribe with whisper via helper script
    print(f"  Transcrevendo {base}...")
    out, err, code = run(f'{WHISPER_ENV} {TRANSCRIBE_PY} "{wav}" "{out_md}"', timeout=1800)
    
    if code != 0 or not os.path.exists(out_md):
        print(f"  ERRO transcricao: {base}: {err[:200]}")
        # Try without language hint
        with open(TRANSCRIBE_PY, 'w') as f:
            f.write('''#!/usr/bin/env python3
import os, sys
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
from faster_whisper import WhisperModel
wav_path = sys.argv[1]
out_path = sys.argv[2]
model = WhisperModel('base', device='cpu', compute_type='int8')
segments, info = model.transcribe(wav_path)
texts = []
for seg in segments:
    texts.append(f"[{seg.start:.1f}s - {seg.end:.1f}s] " + seg.text)
result = "\\n".join(texts)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write("# Transcricao\\n\\n")
    f.write(result + "\\n")
print(f"OK: {len(result)} chars -> {out_path}")
''')
        out, err, code = run(f'{WHISPER_ENV} {TRANSCRIBE_PY} "{wav}" "{out_md}"', timeout=1800)
    
    if os.path.exists(out_md):
        os.remove(wav)
        kb = os.path.getsize(out_md) // 1024
        print(f"  OK: {safe}.md ({kb}KB)")
        return out_md
    else:
        print(f"  FALHA: {base}")
        return None

# Find all .m4a files
m4as = glob.glob(os.path.join(TT_AUDIO, "*.m4a"))
m4as += glob.glob(os.path.join(TT_BANCADAS, "*.m4a"))
m4as = [f for f in m4as if "/site/" not in f]

print(f"Total de audios: {len(m4as)}")
for m in sorted(m4as):
    sz = os.path.getsize(m)//1024//1024
    print(f"  {os.path.basename(m):50s} {sz}MB")

for m4a in sorted(m4as):
    result = transcribe_one(m4a)
    if result:
        print(f"  -> {result}")
    print()
