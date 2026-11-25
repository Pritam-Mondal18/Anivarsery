import os
import re

def fix_file(filepath, replacements):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old, new in replacements:
        content = content.replace(old, new)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

# 1. HTML files in root and public
html_replacements = [
    ('"/assets/', '"./assets/'),
    ("'/assets/", "'./assets/"),
    ('src="/assets/', 'src="./assets/'),
    ('href="/assets/', 'href="./assets/'),
    ('content="/assets/', 'content="./assets/'),
    ('href="/#events"', 'href="./#events"'),
    ('event-pages.css?v=6', 'event-pages.css?v=7'),
    ('app.js?v=30', 'app.js?v=31'),
    ('app.css?v=30', 'app.css?v=31'),
]

for h in ['index.html', 'ashirbad.html', 'biye.html', 'boubhat.html', 'gaye-holud.html',
          'public/ashirbad.html', 'public/biye.html', 'public/boubhat.html', 'public/gaye-holud.html']:
    fix_file(h, html_replacements)

# 2. CSS files
css_replacements = [
    ("url('/assets/", "url('./"),
    ('url("/assets/', 'url("./'),
    ('url(/assets/', 'url(./'),
]

for c in ['assets/app.css', 'public/assets/app.css', 'assets/event-pages.css', 'public/assets/event-pages.css']:
    fix_file(c, css_replacements)

# 3. JS files
js_replacements = [
    ('"/assets/', '"./assets/'),
    ("'/assets/", "'./assets/"),
    ('"/ashirbad.html"', '"./ashirbad.html"'),
    ('"/gaye-holud.html"', '"./gaye-holud.html"'),
    ('"/biye.html"', '"./biye.html"'),
    ('"/boubhat.html"', '"./boubhat.html"'),
    ("'/' + Q(x.img) + '.html'", "'./' + Q(x.img) + '.html'"),
]

for j in ['assets/app.js', 'public/assets/app.js']:
    fix_file(j, js_replacements)

print("All path fixes completed.")
