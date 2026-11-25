import re
import json

with open('gaye-holud.html', 'r', encoding='utf-8') as f:
    text = f.read()

card_count = text.count('class="ep-card"')
print('Count of ep-card in gaye-holud.html:', card_count)

m = re.search(r'const photos = (\[.*?\]);', text)
if m:
    photos = json.loads(m.group(1))
    print(f'Photos in gaye-holud.html: {len(photos)}')
    for i, p in enumerate(photos):
        print(f"[{i+1}] {p['src']} : {p['title']} - {p['sub']}")
else:
    print('Error: photos not matched')

with open('assets/app.js', 'r', encoding='utf-8') as f:
    app_text = f.read()

m_app = re.search(r'"event-holud":\s*\{.*?photos:\s*\[(.*?)\]\s*\}', app_text, re.DOTALL)
if m_app:
    print('Found photos in app.js event-holud! Length of block:', len(m_app.group(1)))
    lines = [l.strip() for l in m_app.group(1).splitlines() if l.strip()]
    print('Item count in app.js:', len(lines))
else:
    print('Error matching event-holud in app.js')
