import json
import re

photos_data = [
    {
        "src": "/assets/bouvat/bv1.jpeg",
        "title": "নববধূর রূপের ছটা",
        "sub": "ম্যাজেন্টা বেনারসী ও স্বর্ণালংকারে চন্দনার অপরূপ ব্রাইডাল সাজ",
        "pos": "center 20%"
    },
    {
        "src": "/assets/bouvat/bv2.jpeg",
        "title": "মায়ের স্নেহের পরশ",
        "sub": "মমতাময়ী আলিঙ্গনে আবেগঘন ভালোবাসা ও আশীর্বাদ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv3.jpeg",
        "title": "ভাই-বোনদের সাথে যুগল",
        "sub": "স্টেজের আলোয় নবদম্পতির সাথে ভাই-বোনেদের আনন্দক্ষণ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv4.jpeg",
        "title": "স্বপ্নের যুগলবন্দী",
        "sub": "নীল স্যুট ও টুকটুকে বেনারসীতে অর্ণব ও চন্দনার রাজকীয় রূপ",
        "pos": "center 20%"
    },
    {
        "src": "/assets/bouvat/bv5.jpeg",
        "title": "একান্ত অনুভূতির রঙ",
        "sub": "একে অপরের পাশে দাঁড়িয়ে জীবনের নতুন অধ্যায়ের সূচনা",
        "pos": "center 25%"
    },
    {
        "src": "/assets/bouvat/bv6.jpeg",
        "title": "দিদা ও নাতনির খুনসুটি",
        "sub": "মুখে চওড়া হাসি আর বুকে একরাশ স্নেহের গভীর টান",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv7.jpeg",
        "title": "বাবার স্নেহের নীড়",
        "sub": "বাবার অকৃত্রিম ভালোবাসার নিরাপদ আশ্রয় ও আশীর্বাদ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv8.jpeg",
        "title": "পিতামাতার নয়নমণি",
        "sub": "বাবা ও মায়ের যৌথ আশীর্বাদে নববধূর জীবনের পরম পাওয়া",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv9.jpeg",
        "title": "ভাই ও বন্ধুদের আড্ডা",
        "sub": "স্টাইলিশ স্যুট ও রঙিন পোশাকে বন্ধুদের প্রাণোচ্ছ্বল উপস্থিতি",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv10.jpeg",
        "title": "ছোটদের সাথে আনন্দমেলা",
        "sub": "স্নেহের ছোট ভাইদের মিষ্টি উপস্থিতি ও মিষ্টি স্মিত হাসি",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv11.jpeg",
        "title": "ভাইয়ের চোখের মণি",
        "sub": "দিদি আর ভাইয়ের আজীবন অটুট বন্ধন ও স্নেহের স্মৃতি",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv12.jpeg",
        "title": "বন্ধুত্বের রঙিন ফ্রেম",
        "sub": "অনুষ্ঠানের মঞ্চে ভাই ও বন্ধুদের প্রাণবন্ত ক্যামেরাবন্দী মুহূর্ত",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv13.jpeg",
        "title": "একান্নবর্তী পরিবারের মিলন",
        "sub": "বড়-ছোট সবার যৌথ হাসিতে এক অনন্য পারিবারিক স্মৃতি",
        "pos": "center 35%"
    },
    {
        "src": "/assets/bouvat/bv14.jpeg",
        "title": "আত্মীয় পরিজনের সমাগম",
        "sub": "স্নেহময়ী মাসি, পিসি ও কাকিমাদের সাথে হাসিমুখের স্মৃতি",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv15.jpeg",
        "title": "গুরুজনদের শুভাশিস",
        "sub": "নতুন সংসারের যাত্রাপথে পরিবারের বয়োজ্যেষ্ঠদের আশীর্বাদ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv16.jpeg",
        "title": "তারুণ্যের কলকাকলি",
        "sub": "ভাই-বোন ও সমবয়সীদের হাসিখুশি আড্ডা ও অনাবিল আনন্দ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv17.jpeg",
        "title": "পিতামাতা ও পরিজনের আশীর্বাদ",
        "sub": "বাবা-মা ও গুরুজনদের উপস্থিতিতে এক পূর্ণাঙ্গ পারিবারিক ছবি",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv18.jpeg",
        "title": "ভাই ও অনুজদের সাথে খুনসুটি",
        "sub": "ছোটদের মিষ্টি সাজ আর কচি মুখের নির্মল হাসি",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv19.jpeg",
        "title": "ছোট ভাইয়ের মিষ্টি সঙ্গ",
        "sub": "স্নেহের ছোট ভাইয়ের সাথে দিদির অকৃত্রিম ভালোবাসার ছবি",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv20.jpeg",
        "title": "গুরুজনের স্নেহচ্ছায়া",
        "sub": "নবদম্পতির মাথায় গুরুজনদের স্নেহের স্পর্শ ও শুভকামনা",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv21.jpeg",
        "title": "ভাই ও বন্ধুদের শুভকামনা",
        "sub": "সুসজ্জিত মঞ্চে নতুন বৌদির সাথে ভাই ও বন্ধুদের ছবি",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv22.jpeg",
        "title": "বন্ধু ও ভাইদের মেলা",
        "sub": "অফুরন্ত হাসি আর আন্তরিক আড্ডায় মুখর সংবর্ধনা মঞ্চ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/bouvat/bv23.jpeg",
        "title": "পারিবারিক মেলবন্ধন",
        "sub": "এক ফ্রেমে ভালোবাসা, আন্তরিকতা ও সৌহার্দ্যের মধুর মেলবন্ধন",
        "pos": "center 35%"
    },
    {
        "src": "/assets/bouvat/bv24.jpeg",
        "title": "স্নেহের নিবিড় আলিঙ্গন",
        "sub": "হৃদয়ের উষ্ণ স্পর্শ আর ভালোবাসায় সিক্ত স্মরণীয় মুহূর্ত",
        "pos": "center 30%"
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

new_grid_content = "\n" + "\n".join(cards_html_list) + "\n      "

photos_json = json.dumps([{"src": p["src"], "title": p["title"], "sub": p["sub"]} for p in photos_data], ensure_ascii=False)

def update_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update CSS link query param
    content = re.sub(r'event-pages\.css\?v=\d+', 'event-pages.css?v=6', content)

    # Replace grid cards
    # Search for <div class="ep-grid"> ... </div> before </section>
    grid_pattern = r'(<div class="ep-grid">)[\s\S]*?(</div>\s*</section>)'
    content = re.sub(grid_pattern, r'\1' + new_grid_content + r'\2', content)

    # Replace epLbCounter initial text
    counter_pattern = r'<span id="epLbCounter" class="ep-lb__counter">\d+ / \d+</span>'
    content = re.sub(counter_pattern, f'<span id="epLbCounter" class="ep-lb__counter">1 / {len(photos_data)}</span>', content)

    # Replace photos array in <script>
    script_pattern = r'const photos = \[[\s\S]*?\];'
    content = re.sub(script_pattern, f'const photos = {photos_json};', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_html_file('boubhat.html')
update_html_file('public/boubhat.html')

# Update assets/app.js and public/assets/app.js
def update_js_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Locate "event-boubhat": { ... photos: [ ... ] ... }
    # We replace photos: [ ... ] inside "event-boubhat"
    boubhat_pattern = r'("event-boubhat"\s*:\s*\{[\s\S]*?photos\s*:\s*)\[[\s\S]*?\](\s*\})'
    
    js_photos_formatted = json.dumps([{"src": p["src"], "title": p["title"], "sub": p["sub"]} for p in photos_data], ensure_ascii=False, indent=8)
    # indent fix
    replacement = r'\g<1>' + js_photos_formatted + r'\g<2>'
    content = re.sub(boubhat_pattern, replacement, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_js_file('assets/app.js')
update_js_file('public/assets/app.js')

# Update index.html version query parameter (?v=27 -> ?v=28)
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_content = re.sub(r'app\.js\?v=27', 'app.js?v=28', idx_content)
idx_content = re.sub(r'app\.css\?v=27', 'app.css?v=28', idx_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Updated index.html (?v=28)")
