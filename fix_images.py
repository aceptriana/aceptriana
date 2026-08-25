import re

target_file = 'C:/Users/Acep/aceptriana/README.md'
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

new_content = re.sub(
    r'(<img src="https://cdn\.jsdelivr\.net/gh/devicons/[^"]+" alt="[^"]+") (class="[^"]+")',
    r'\1 width="48" height="48" \2',
    content
)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(new_content)
