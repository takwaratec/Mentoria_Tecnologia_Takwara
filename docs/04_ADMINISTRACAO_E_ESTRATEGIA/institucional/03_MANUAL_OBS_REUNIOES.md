# 🎙️ OBS Studio — Manual Rápido para Gravação de Reuniões

> **OBS Studio** = Open Broadcaster Software — gratuito, código aberto.
> Ideal para gravar reuniões Zoom/Meet/Teams com qualidade local, sem depender da nuvem.

---

## 1. Instalação

**Download direto (link oficial):**
- https://obsproject.com/pt-br/download (escolher macOS Intel)

Ou via navegador: obsproject.com → Download → macOS

> ⚠️ Se o brew falhar, baixe manualmente do site e arraste para a pasta Applications.

---

## 2. Preset: "Reunião Takwara"

Ao abrir o OBS pela primeira vez, siga:

### 2.1 Configurar cena

1. Abra o OBS → na caixa **Cenas** (inferior esquerdo), clique **+**
2. Nome: `Reuniao Takwara`
3. Na caixa **Fontes**, clique **+** → **Captura de Áudio (Input)** → selecione seu microfone
4. Se quiser gravar a tela compartilhada: clique **+** → **Captura de Tela (Display Capture)** → selecione o monitor

### 2.2 Configurar gravação apenas de áudio (para reuniões)

Se quiser gravar SÓ O ÁUDIO (mais leve):

1. Clique com botão direito na fonte de vídeo (se houver) → **Remover**
2. Mantenha apenas a fonte **Captura de Áudio (Input)**

### 2.3 Configurar qualidade

Vá em **Arquivo → Configurações → Saída**:

| Parâmetro | Valor |
|---|---|
| **Modo de Saída** | Avançado |
| **Gravação → Tipo de codificador** | AAC |
| **Bitrate de áudio** | 128 kbps |
| **Caminho de gravação** | `~/Áudio Reuniões/` (criar pasta) |
| **Formato de gravação** | `.mp4` (ou `.mkv` à prova de falhas) |

### 2.4 Atalhos úteis

| Função | Atalho padrão |
|---|---|
| Iniciar gravação | `Cmd + R` |
| Parar gravação | `Cmd + R` |
| Pausar | `Cmd + Shift + P` |

---

## 3. Fluxo de trabalho

### Antes da reunião

```bash
# 1. Abrir OBS
open -a OBS

# 2. Verificar microfone na fonte de áudio
# (a barra de áudio no mixer deve se movimentar quando você fala)
```

### Durante a reunião

1. Ao entrar na chamada, aperte **Cmd + R** para começar a gravar
2. No final, **Cmd + R** para parar
3. O arquivo estará na pasta configurada

### Após a reunião — Transcrição

```bash
# 1. Extrair áudio (caso tenha gravado MP4 com vídeo)
ffmpeg -i reuniao.mp4 -ar 16000 -ac 1 reuniao.wav -y

# 2. Transcrever (faster-whisper)
export KMP_DUPLICATE_LIB_OK=TRUE
/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3 -c "
from faster_whisper import WhisperModel
model = WhisperModel('base', device='cpu', compute_type='int8')
segments, info = model.transcribe('caminho/do/arquivo.wav', language='pt')
for seg in segments:
    print(f'[{seg.start:.1f}s] {seg.text}')
"

# 3. Decupar → Hermes processa
```

---

## 4. Script de transcrição automática

> Caminho sugerido: `scripts/transcrever_audio.sh`

```bash
#!/bin/bash
# Uso: ./transcrever_audio.sh caminho/do/audio.wav
export KMP_DUPLICATE_LIB_OK=TRUE
/Users/fabiotakwara/miniconda3/envs/whisper_env/bin/python3 /tmp/transcreve_wav.py "$1"
```

---

*Manual preparado por Hermes Agent · Tecnologia Takwara · 30/06/2026*
