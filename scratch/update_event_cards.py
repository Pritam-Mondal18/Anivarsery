import re

old_events = '''events: [{ bn: "আশীর্বাদ", en: "Ashirbad", img: "event-ashirbad", icon: "thala", when: "Wednesday, 20 January · 11:00 AM", where: ", Behala", mapQuery: "Behala, Kolkata", note: "ধান-দুব্বো আর অনেকটা আশীর্বাদ নিয়ে আসবেন।" }, { bn: "গায়ে হলুদ", en: "Gaye Holud", img: "event-holud", icon: "haldi", when: "Friday, 22 January · 8:00 AM", where: "দু'বাড়িতেই", mapQuery: "Behala, Kolkata", note: "পুরোনো জামা পরে আসাই ভালো, হলুদ লাগবেই।" }, { bn: "বিয়ে", en: "Biye", img: "event-biye", icon: "topor", when: "Friday, 22 January · 7:00 PM", where: "Golap Bagan Banquet, Behala", mapQuery: "Behala, Kolkata", note: "লগ্ন রাত ৯টা ১২-য়।" }, { bn: "বৌভাত", en: "Boubhat", img: "event-boubhat", icon: "kolapata", when: "Sunday, 26 November · 7:30 PM", where: ", Khardha", mapQuery: "Salt Lake, Kolkata", note: "ভাত-কাপড়ের পর জমিয়ে খাওয়াদাওয়া।" }]'''

new_events = '''events: [{ bn: "আশীর্বাদ", en: "Ashirbad", img: "event-ashirbad", icon: "thala", when: "স্নেহ, ভালোবাসা ও গুরুজনদের শুভাশিস", where: "", mapQuery: "", note: "দুটি পরিবারের আন্তরিক মেলবন্ধন ও নতুন পথচলা।" }, { bn: "গায়ে হলুদ", en: "Gaye Holud", img: "event-holud", icon: "haldi", when: "হলুদের রঙে রাঙা আনন্দ ও হাসি-হুল্লোড়", where: "", mapQuery: "", note: "কাঁচা হলুদের সুবাস আর আত্মীয়-বন্ধুদের অফুরন্ত খুনসুটি।" }, { bn: "বিয়ে", en: "Biye", img: "event-biye", icon: "topor", when: "সাতপাকে বাঁধা দুটি মন ও একরাশ স্বপ্ন", where: "", mapQuery: "", note: "শুভদৃষ্টি, মালাবদল আর অগ্নিসাক্ষী রেখে আজীবনের অঙ্গীকার।" }, { bn: "বৌভাত", en: "Boubhat", img: "event-boubhat", icon: "kolapata", when: "ভাত-কাপড়ের দায়িত্ব ও সান্ধ্য প্রীতিভোজ", where: "", mapQuery: "", note: "নতুন আলোয় গৃহপ্রবেশ, আত্মীয় সমাগম ও রাজকীয় সংবর্ধনা।" }]'''

def update_js(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if old_events in content:
        content = content.replace(old_events, new_events)
        print(f"Replaced events successfully in {filepath}")
    else:
        # Fallback regex pattern in case of whitespace difference
        pattern = r'events:\s*\[\{\s*bn:\s*"আশীর্বাদ"[\s\S]*?note:\s*"ভাত-কাপড়ের পর জমিয়ে খাওয়াদাওয়া\।"\s*\}\]'
        if re.search(pattern, content):
            content = re.sub(pattern, new_events, content)
            print(f"Replaced events via regex in {filepath}")
        else:
            print(f"ERROR: old_events pattern not found in {filepath}")
            return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Saved {filepath}")
    return True

update_js('assets/app.js')
update_js('public/assets/app.js')

def update_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    rule = '\n.ev__where:empty{display:none!important;margin:0!important;padding:0!important;}\n'
    if '.ev__where:empty' not in content:
        content += rule
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added .ev__where:empty rule in {filepath}")
    else:
        print(f"Rule already in {filepath}")

update_css('assets/app.css')
update_css('public/assets/app.css')

# Bump version in index.html to ?v=30
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_content = idx_content.replace('app.js?v=29', 'app.js?v=30')
idx_content = idx_content.replace('app.css?v=29', 'app.css?v=30')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Updated index.html to ?v=30")
