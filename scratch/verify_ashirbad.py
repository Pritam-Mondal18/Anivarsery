import re
import json

with open('ashirbad.html', 'r', encoding='utf-8') as f:
    text = f.read()

card_count = text.count('class="ep-card"')
print('Count of ep-card in ashirbad.html:', card_count)

m = re.search(r'const photos = (\[.*?\]);', text)
if m:
    photos = json.loads(m.group(1))
    print(f'Photos in ashirbad.html: {len(photos)}')
    for i, p in enumerate(photos):
        print(f"[{i}] {p['src']} : {p['title']} - {p['sub']}")
else:
    print('Error: photos not matched')

with open('assets/app.js', 'r', encoding='utf-8') as f:
    app_text = f.read()

idx = app_text.find('"event-ashirbad"')
print('\napp.js event-ashirbad slice:')
print(app_text[idx:idx+650])
