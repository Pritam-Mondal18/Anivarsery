import os
import json
import re

photos_data = [
    {
        "src": "/assets/gayeholud/h1.jpeg",
        "title": "বরণ ডালা ও মাঙ্গলিক সাজ",
        "sub": "আলপনা আঁকা সরা, মিষ্টি ও সিঁদুর কৌটোয় সাজানো আচার",
        "pos": "center center"
    },
    {
        "src": "/assets/gayeholud/h2.jpeg",
        "title": "কনে সাজ ও মুকুট পরানো",
        "sub": "মাথায় শোলার মুকুট আর অন্তরের গভীর আশীর্বাদ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/gayeholud/h3.jpeg",
        "title": "স্নেহের অভিষেক ও আশীর্বাদ",
        "sub": "পরম শ্রদ্ধায় বড়দের মঙ্গলকামনা গ্রহণ",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h4.jpeg",
        "title": "ভাই ও বন্ধুদের বাঁধভাঙা উল্লাস",
        "sub": "হলুদ পাঞ্জাবিতে নাচের তালে উৎসবের মেজাজ",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h5.jpeg",
        "title": "জল সওয়ার মঙ্গল শোভাযাত্রা",
        "sub": "হলুদ শাড়িতে মা ও বোনেদের উলুধ্বনি ও আনন্দ",
        "pos": "center 30%"
    },
    {
        "src": "/assets/gayeholud/h6.jpeg",
        "title": "ঢাকের তালে উদ্দাম নাচ",
        "sub": "পাড়ার পথে সবার সাথে খুশির বাঁধভাঙা জোয়ার",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h7.jpeg",
        "title": "ঘাট বরণ ও পবিত্র জল স্পর্শ",
        "sub": "হাতপাখা দিয়ে পুকুর ঘাটে ঐতিহ্যবাহী মাঙ্গলিক নিয়ম",
        "pos": "center 30%"
    },
    {
        "src": "/assets/gayeholud/h8.jpeg",
        "title": "হাসিমুখে নাচের আনন্দ",
        "sub": "বরণ ডালা হাতে পরিবারের সবার উচ্ছ্বসিত নাচ",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h9.jpeg",
        "title": "স্নেহের ছোঁয়ায় কাঁচা হলুদ",
        "sub": "প্রিয়জনদের ভালোবাসার পরশে উজ্জ্বল কনেমুখ",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h10.jpeg",
        "title": "আদরের স্পর্শে হলুদ বরণ",
        "sub": "দিদি ও প্রিয়জনেদের মিষ্টি ভালোবাসায় জড়ানো মুহূর্ত",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h11.jpeg",
        "title": "গোলাপের পাপড়ির বৃষ্টি",
        "sub": "একরাশ রঙিন আনন্দ ও বিজয়ের অমলিন হাসি",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h12.jpeg",
        "title": "পবিত্র ঘটের পুণ্য স্নান",
        "sub": "গঙ্গার পুণ্য বারি ঢেলে মাঙ্গলিক হলুদ স্নান",
        "pos": "center 35%"
    },
    {
        "src": "/assets/gayeholud/h13.jpeg",
        "title": "পুণ্য বারি ও স্নানের আচার",
        "sub": "মঙ্গল ঘটের জলে শুদ্ধতার পবিত্র ধারা",
        "pos": "center 35%"
    },
    {
        "src": "/assets/gayeholud/h14.jpeg",
        "title": "জেঠু-জেঠির স্নেহের ছায়ায়",
        "sub": "মাটির মানুষের অন্তরের ভালোবাসা ও আশীর্বাদ",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h15.jpeg",
        "title": "ভাইদের ভালোবাসার ঘেরাটোপে",
        "sub": "দিদির শুভদিনে ভাই ও বন্ধুদের আন্তরিক সান্নিধ্য",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h16.jpeg",
        "title": "পদ্মপীঠে পুরো পরিবার",
        "sub": "পরিবারের সবার সাথে উল্লাস ও ভালোবাসার মিলনমেলা",
        "pos": "center 30%"
    },
    {
        "src": "/assets/gayeholud/h17.jpeg",
        "title": "আনন্দের ফোয়ারা",
        "sub": "গোলাপের সুবাস আর পুষ্পবৃষ্টির মিষ্টি আমেজ",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h18.jpeg",
        "title": "শোভাযাত্রার সুন্দর মুহূর্ত",
        "sub": "হলুদ রোদ্দুরে সাজানো একান্নবর্তী পরিবারের ফ্রেম",
        "pos": "center 30%"
    },
    {
        "src": "/assets/gayeholud/h19.jpeg",
        "title": "দিদি ও বোনেদের মিষ্টি খুনসুটি",
        "sub": "হলুদ সাজে বোনদের অফুরন্ত আন্তরিকতা ও আদর",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h20.jpeg",
        "title": "ভাইয়ের সাথে বোনের মায়ার বন্ধন",
        "sub": "জীবনের প্রতিটি পদক্ষেপে পাশে থাকার মিষ্টি প্রতিশ্রুতি",
        "pos": "center 20%"
    },
    {
        "src": "/assets/gayeholud/h21.jpeg",
        "title": "ছোটদের সাথে আদরের সময়",
        "sub": "পরিবারের ছোট সদস্য ও প্রিয়জনেদের সাথে স্নিগ্ধ হাসিমুখ",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h22.jpeg",
        "title": "আপনজনদের ভালোবাসা",
        "sub": "আত্মীয়-পরিজনের শুভকামনায় উজ্জ্বল প্রতিটি ক্ষণ",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h24.jpeg",
        "title": "ভ্রাতৃস্নেহের নির্ভরতা",
        "sub": "দিদির নতুন জীবনের সূচনায় ভাইয়ের গর্ব ও ভালোবাসা",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h25.jpeg",
        "title": "আলতা রাঙা দুটি চরণ",
        "sub": "রূপোর নূপুর আর গোলাপের পাপড়িতে সাজানো মাঙ্গলিক পদচিহ্ন",
        "pos": "center 40%"
    },
    {
        "src": "/assets/gayeholud/h26.jpeg",
        "title": "সখীর সাথে হাসিমুখের আড্ডা",
        "sub": "ছোটবেলার স্মৃতি আর চিরন্তন বন্ধুত্বের ছোঁয়া",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h27.jpeg",
        "title": "প্রাণখোলা বন্ধুত্বের বন্ধন",
        "sub": "প্রিয় বান্ধবীর সান্নিধ্যে একঝাঁক নির্মল আনন্দের হাসি",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h28.jpeg",
        "title": "শাঁখা-পলা ও সোনার কঙ্কণ",
        "sub": "মেহেন্দির সুক্ষ্ম আলপনায় বাঙালি বধূর ঐতিহ্য",
        "pos": "center 40%"
    },
    {
        "src": "/assets/gayeholud/h29.jpeg",
        "title": "মাঙ্গলিক লাল গাছকৌটো",
        "sub": "সিঁদুরের পবিত্রতা ও বাঙালি বিবাহের শুভ প্রতীক",
        "pos": "center 40%"
    },
    {
        "src": "/assets/gayeholud/h30.jpeg",
        "title": "কনের অপরূপ স্নিগ্ধ রূপ",
        "sub": "লাল পেড়ে শাড়িতে গাছকৌটো হাতে বাংলার চিরায়ত কনে",
        "pos": "center 25%"
    },
    {
        "src": "/assets/gayeholud/h31.jpeg",
        "title": "লাজুক নয়নে শুভদৃষ্টির অপেক্ষা",
        "sub": "কপালে গাছকৌটোর শুভস্পর্শ আর হৃদয়ে আগামীর স্বপ্ন",
        "pos": "center 20%"
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
    new_html = re.sub(r'<span id="epLbCounter" class="ep-lb__counter">.*?</span>', '<span id="epLbCounter" class="ep-lb__counter">1 / 31</span>', new_html)

    # Replace const photos = [...]
    new_html = re.sub(r'const photos = \[.*?\];', f'const photos = {js_photos_json};', new_html, flags=re.DOTALL)

    # Bump CSS version
    new_html = new_html.replace('/assets/event-pages.css?v=5', '/assets/event-pages.css?v=6')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Successfully updated {filepath}")

update_html('gaye-holud.html')
update_html('public/gaye-holud.html')

# Update app.js and public/assets/app.js
def update_app_js(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find "event-holud": { ... photos: [ ... ]
    m = re.search(r'("event-holud"\s*:\s*\{.*?photos\s*:\s*\[).*?(\]\s*\})', content, re.DOTALL)
    if not m:
        print(f"Error: event-holud not found in {filepath}")
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
