with open('assets/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = re.findall(r'["\']/assets/[^"\']+["\']', js)
print('Count of /assets/ in app.js:', len(matches))
print('Sample in app.js:', matches[:15])

# Also check html files
for h in ['index.html', 'ashirbad.html', 'biye.html', 'boubhat.html', 'gaye-holud.html']:
    with open(h, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.findall(r'["\']/assets/[^"\']+["\']', content)
    print(f'{h}: {len(m)} matches')
