import re

file_path = "01_TRIAGEM_BRUTA/WhatsApp Chat - Raízes - Grupo de Entrada - Junho 26/_chat.txt"

users = {}
current_user = None
pattern = re.compile(r'^\[\d{2}/\d{2}/\d{4} \d{2}:\d{2}:\d{2}\] ([^:]+): (.*)')

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        match = pattern.match(line)
        if match:
            user = match.group(1).replace("~\u202f", "").strip()
            msg = match.group(2).strip()
            if "entrou usando o link" in msg or "mudou a descrição" in msg:
                continue
            current_user = user
            if user not in users:
                users[user] = []
            users[user].append(msg)
        else:
            if current_user:
                users[current_user].append(line)

intro_keywords = ["sou", "me chamo", "meu nome", "formada em", "trabalho com", "ajudo", "moro em", "mentoria", "Instagram", "@"]

summary = []
for user, msgs in users.items():
    text = " ".join(msgs)
    if len(text) > 80:
        # Check if it looks like an intro
        lower_text = text.lower()
        if sum(1 for kw in intro_keywords if kw in lower_text) >= 2:
            summary.append(f"### {user}\n{text}\n")

with open("01_TRIAGEM_BRUTA/intros_summary.md", "w", encoding="utf-8") as out:
    out.write("\n".join(summary))

print(f"Extracted {len(summary)} intros.")
