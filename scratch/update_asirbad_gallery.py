import os
import json
import re

photos_data = [
    {
        "src": "/assets/asirbad/a1.jpeg",
        "title": "ধান-দূর্বায় শুভাশিস",
        "sub": "মাঙ্গলিক আচার ও বড়দের অন্তরের পরম আশীর্বাদ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/asirbad/a2.jpeg",
        "title": "একসাথে পথচলার সূচনা",
        "sub": "স্নেহ ও প্রীতিতে উজ্জ্বল দুটি ভালোবাসার মুখ",
        "pos": "center 25%"
    },
    {
        "src": "/assets/asirbad/a3.jpeg",
        "title": "প্রদীপ ও মঙ্গল স্পর্শ",
        "sub": "নতুন জীবনের শুরুতে আলো ও শুভকামনার ছোঁয়া",
        "pos": "center 40%"
    },
    {
        "src": "/assets/asirbad/a4.jpeg",
        "title": "স্নেহের উষ্ণ আলিঙ্গন",
        "sub": "মায়ের আদরে জড়ানো এক অমূল্য মুহূর্ত",
        "pos": "center 25%"
    },
    {
        "src": "/assets/asirbad/a5.jpeg",
        "title": "হাসিমুখের সুন্দর বন্ধন",
        "sub": "পারিবারিক ভালোবাসা আর একরাশ মধুর আনন্দ",
        "pos": "center 25%"
    },
    {
        "src": "/assets/asirbad/a6.jpeg",
        "title": "চিরদিনের প্রতিশ্রুতি",
        "sub": "হাতে হাত রেখে অটুট বিশ্বাস আর ভালোবাসা",
        "pos": "center 20%"
    },
    {
        "src": "/assets/asirbad/a7.jpeg",
        "title": "জমজমাট সেলফি মোমেন্ট",
        "sub": "ভাই-বোন ও পরিবার পরিজনের খুনসুটি ও আনন্দ",
        "pos": "center center"
    },
    {
        "src": "/assets/asirbad/a8.jpeg",
        "title": "মাঙ্গলিক বরণ ও শুভকামনা",
        "sub": "পরম শ্রদ্ধায় বড়দের আশীর্বাদ গ্রহণ",
        "pos": "center 35%"
    },
    {
        "src": "/assets/asirbad/a9.jpeg",
        "title": "চন্দন ও স্নেহস্পর্শ",
        "sub": "অন্তরের গভীর থেকে দেওয়া পবিত্র মঙ্গলধ্বনি",
        "pos": "center 30%"
    },
    {
        "src": "/assets/asirbad/a10.jpeg",
        "title": "আচারের পবিত্র ডালি",
        "sub": "ধান-দূর্বা, পান ও মিষ্টিতে সাজানো ঐতিহ্য",
        "pos": "center 35%"
    },
    {
        "src": "/assets/asirbad/a11.jpeg",
        "title": "গুরুজনদের ছায়ায়",
        "sub": "স্নেহের পরশে নিশ্চিন্ত আগামীর দিনগুলি",
        "pos": "center 25%"
    },
    {
        "src": "/assets/asirbad/a12.jpeg",
        "title": "দুই পরিবারের মধুর মিলন",
        "sub": "সবার আশীর্বাদ ও ভালোবাসায় পরিপূর্ণ আমাদের সংসার",
        "pos": "center 35%"
    }
]

# Generate grid cards HTML
cards_html_list = []
for idx, p in enumerate(photos_data):
    card = f'''        <div class="ep-card" onclick="openLightbox({idx})">
          <div class="ep-card__img-wrap">
            <img src="{p['src']}" alt="{p['title']}" loading="lazy" style="object-position: {p['pos']};" />
            <div class="ep-card__zoom-hint">
              <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="7" />
                <line x1="21" y1="21" x2="16.65" y2="16.65" />
                <line x1="11" y1="8" x2="11" y2="14" />
                <line x1="8" y1="11" x2="14" y2="11" />
              </svg>
              <span>জুম করুন</span>
            </div>
          </div>
          <div class="ep-card__caption">
            <span class="ep-card__title">{p['title']}</span>
            <span class="ep-card__sub">{p['sub']}</span>
          </div>
        </div>'''
    cards_html_list.append(card)

grid_cards_html = '\n'.join(cards_html_list)

# Generate JS photos JSON
js_photos_json = json.dumps([{"src": p["src"], "title": p["title"], "sub": p["sub"]} for p in photos_data], ensure_ascii=False)

def update_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace grid content between <div class="ep-grid"> and </div>\n    </section>
    grid_start = html.find('<div class="ep-grid">')
    if grid_start == -1:
        print(f"Error: ep-grid not found in {filepath}")
        return
    grid_content_start = grid_start + len('<div class="ep-grid">\n')
    grid_end = html.find('</div>\n    </section>', grid_content_start)
    if grid_end == -1:
        grid_end = html.find('</div>\r\n    </section>', grid_content_start)

    if grid_end != -1:
        new_html = html[:grid_content_start] + grid_cards_html + '\n      ' + html[grid_end:]
    else:
        print(f"Error finding grid_end in {filepath}")
        return

    # Replace counter
    new_html = re.sub(r'<span id="epLbCounter" class="ep-lb__counter">.*?</span>', '<span id="epLbCounter" class="ep-lb__counter">1 / 12</span>', new_html)

    # Replace const photos = [...]
    new_html = re.sub(r'const photos = \[.*?\];', f'const photos = {js_photos_json};', new_html, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Successfully updated {filepath}")

update_html('ashirbad.html')
update_html('public/ashirbad.html')

# Update app.js and public/assets/app.js
def update_app_js(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find "event-ashirbad": { ... photos: [ ... ]
    m = re.search(r'("event-ashirbad"\s*:\s*\{.*?photos\s*:\s*\[).*?(\]\s*\})', content, re.DOTALL)
    if not m:
        print(f"Error: event-ashirbad not found in {filepath}")
        return

    # Format photos for app.js
    app_photos_lines = []
    for p in photos_data:
        app_photos_lines.append(f'      {{ src: "{p["src"]}", title: "{p["title"]}", sub: "{p["sub"]}" }}')
    app_photos_str = '\n' + ',\n'.join(app_photos_lines) + '\n    '

    new_section = m.group(1) + app_photos_str + m.group(2)
    new_content = content[:m.start()] + new_section + content[m.end():]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully updated {filepath}")

update_app_js('assets/app.js')
update_app_js('public/assets/app.js')
