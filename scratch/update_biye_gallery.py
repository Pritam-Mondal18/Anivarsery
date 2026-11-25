import os
import json
import re

photos_data = [
    {
        "src": "/assets/biye/b1.jpeg",
        "title": "বরের শুভ পদার্পণ",
        "sub": "সুসজ্জিত গাড়িতে চড়ে বিবাহ আসরে আগমন",
        "pos": "center 35%"
    },
    {
        "src": "/assets/biye/b2.jpeg",
        "title": "মাঙ্গলিক বরবরণ",
        "sub": "প্রদীপ ও বরণ ডালার স্নিগ্ধ আলোয় বরকে সাদর অভ্যর্থনা",
        "pos": "center 35%"
    },
    {
        "src": "/assets/biye/b3.jpeg",
        "title": "বরযাত্রী ও আসরে প্রবেশ",
        "sub": "টোপর ও বেলফুলের মালায় সেজে বিবাহ মণ্ডপের পথে",
        "pos": "center 25%"
    },
    {
        "src": "/assets/biye/b4.jpeg",
        "title": "উলুধ্বনিতে বরবরণ",
        "sub": "শঙ্খধ্বনি আর উলুধ্বনিতে মুখরিত শুভ মুহূর্ত",
        "pos": "center 25%"
    },
    {
        "src": "/assets/biye/b5.jpeg",
        "title": "গুরুজনদের শুভাশিস",
        "sub": "ধান-দূর্বা দিয়ে বড়দের অন্তরের পরম আশীর্বাদ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/biye/b6.jpeg",
        "title": "আশীর্বাদের উপহার",
        "sub": "পরম স্নেহে উপহারে সাজিয়ে দেওয়া জামাতাকে",
        "pos": "center center"
    },
    {
        "src": "/assets/biye/b7.jpeg",
        "title": "মা ও পরিজনের সান্নিধ্যে",
        "sub": "বরের মুখে অমলিন হাসি আর পরিবারের স্নেহচ্ছায়া",
        "pos": "center 25%"
    },
    {
        "src": "/assets/biye/b8.jpeg",
        "title": "ছাদনাতলায় শুভ সূচনা",
        "sub": "চিত্রিত বিয়ের কুলা হাতে যুগলের মাঙ্গলিক আচার",
        "pos": "center 20%"
    },
    {
        "src": "/assets/biye/b9.jpeg",
        "title": "বৈদিক শুভ সম্প্রদান",
        "sub": "মন্ত্রোচ্চারণে আম্রপল্লবে দুটি হাতের আজীবন মিলন",
        "pos": "center center"
    },
    {
        "src": "/assets/biye/b10.jpeg",
        "title": "পরম পবিত্র সিঁদুরদান",
        "sub": "লজ্জাবস্ত্রের আড়ালে সিঁথিতে রাঙা সিঁদুরের অমর স্পর্শ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/biye/b11.jpeg",
        "title": "সিঁদুররাঙা অমলিন হাসি",
        "sub": "নতুন অধ্যায়ের প্রথম মুহূর্তে আনন্দময় যুগলবন্দী",
        "pos": "center 25%"
    },
    {
        "src": "/assets/biye/b12.jpeg",
        "title": "গুরুজনদের চরণস্পর্শ",
        "sub": "শ্রদ্ধার সাথে প্রণাম ও নতুন জীবনের আশীর্বাদ প্রার্থনা",
        "pos": "center 30%"
    },
    {
        "src": "/assets/biye/b13.jpeg",
        "title": "ভ্রাতৃস্নেহের রাজকীয় ফ্রেম",
        "sub": "লাল বেনারসী পরা দিদির পাশে ভাইয়ের মিষ্টি উপস্থিতি",
        "pos": "center 25%"
    },
    {
        "src": "/assets/biye/b14.jpeg",
        "title": "বস্ত্রদান ও বর সম্মান",
        "sub": "কন্যার পিতার হাত থেকে জামাতাকে মাঙ্গলিক বস্ত্র অর্পণ",
        "pos": "center 35%"
    },
    {
        "src": "/assets/biye/b15.jpeg",
        "title": "নয়নে নয়নে শুভদৃষ্টি",
        "sub": "পান পাতার আড়াল সরিয়ে চোখের ভাষায় প্রথম প্রণয়",
        "pos": "center 25%"
    },
    {
        "src": "/assets/biye/b16.jpeg",
        "title": "পরিবার পরিজনের সাথে কনে",
        "sub": "স্নেহের স্পর্শে আশীর্বাদের ছায়ায় ঘেরা শুভ সন্ধ্যা",
        "pos": "center 25%"
    },
    {
        "src": "/assets/biye/b17.jpeg",
        "title": "মালাবদলের আনন্দ ও খুনসুটি",
        "sub": "আত্মীয়দের কাঁধে চড়ে হাসিমুখে মালা পরাবার মুহূর্ত",
        "pos": "center 30%"
    },
    {
        "src": "/assets/biye/b18.jpeg",
        "title": "ভাইদের ভালোবাসায় কনে",
        "sub": "শুভদিনে আদরের দিদির পাশে ভাইদের স্মৃতির ফ্রেম",
        "pos": "center 25%"
    },
    {
        "src": "/assets/biye/b19.jpeg",
        "title": "রূপসী বাঙালি বধূ",
        "sub": "সিঁদুররাঙা কপাল আর লাল বেনারসীতে অপরূপা চন্দনা",
        "pos": "center 25%"
    },
    {
        "src": "/assets/biye/b20.jpeg",
        "title": "চিরন্তন ভালোবাসার বাঁধন",
        "sub": "বুকভরা নির্ভরতায় অর্ণব ও চন্দনার একাত্ব হওয়া",
        "pos": "center 25%"
    },
    {
        "src": "/assets/biye/b21.jpeg",
        "title": "সুসজ্জিত বিয়ের তত্ত্ব",
        "sub": "শাড়ি, মিষ্টি ও উপহারে সাজানো ঐতিহ্যের ডালি",
        "pos": "center center"
    },
    {
        "src": "/assets/biye/b22.jpeg",
        "title": "বরবরণের শোভাযাত্রা",
        "sub": "মিষ্টি ও বরণ ডালা হাতে মায়েদের হাসিমুখের ভিড়",
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
    new_html = re.sub(r'<span id="epLbCounter" class="ep-lb__counter">.*?</span>', '<span id="epLbCounter" class="ep-lb__counter">1 / 22</span>', new_html)

    # Replace const photos = [...]
    new_html = re.sub(r'const photos = \[.*?\];', f'const photos = {js_photos_json};', new_html, flags=re.DOTALL)

    # Bump CSS version
    new_html = new_html.replace('/assets/event-pages.css?v=5', '/assets/event-pages.css?v=6')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Successfully updated {filepath}")

update_html('biye.html')
update_html('public/biye.html')

# Update app.js and public/assets/app.js
def update_app_js(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find "event-biye": { ... photos: [ ... ]
    m = re.search(r'("event-biye"\s*:\s*\{.*?photos\s*:\s*\[).*?(\]\s*\})', content, re.DOTALL)
    if not m:
        print(f"Error: event-biye not found in {filepath}")
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
