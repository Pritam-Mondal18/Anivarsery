import re

def update_js(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Clear parents values in data
    content = content.replace('parents: "Mitali & Subrata Sen"', 'parents: ""')
    content = content.replace('parents: "Rupa & Debashis Mukherjee"', 'parents: ""')

    # 2. Replace the JSX rendering of Daughter of / Son of
    target_bride = 'c.jsxs("p", { className: "hero__parent hx", children: ["Daughter of ", c.jsx("span", { "data-k": "couple.bride.parents" })] })'
    replacement_bride = 'c.jsx("p", { className: "hero__parent hx", style: { display: "none" } })'
    if target_bride in content:
        content = content.replace(target_bride, replacement_bride)
        print(f"Replaced bride parent element in {filepath}")
    else:
        print(f"WARNING: target_bride not found in {filepath}")

    target_groom = 'c.jsxs("p", { className: "hero__parent hx", children: ["Son of ", c.jsx("span", { "data-k": "couple.groom.parents" })] })'
    replacement_groom = 'c.jsx("p", { className: "hero__parent hx", style: { display: "none" } })'
    if target_groom in content:
        content = content.replace(target_groom, replacement_groom)
        print(f"Replaced groom parent element in {filepath}")
    else:
        print(f"WARNING: target_groom not found in {filepath}")

    # 3. Clean sub caption in setupRegistryLightbox
    content = content.replace('sub: "মিতালি ও সুব্রত মণ্ডলের মেয়ে"', 'sub: ""')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath}")

update_js('assets/app.js')
update_js('public/assets/app.js')

def update_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Append .hero__parent { display: none !important; }
    if '.hero__parent{display:none!important}' not in content:
        content += '\n.hero__parent{display:none!important;visibility:hidden!important;height:0!important;margin:0!important;padding:0!important;opacity:0!important;}\n'
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath} with display:none rule")
    else:
        print(f"Rule already in {filepath}")

update_css('assets/app.css')
update_css('public/assets/app.css')

# Bump version in index.html to v=29
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

idx_content = idx_content.replace('app.js?v=28', 'app.js?v=29')
idx_content = idx_content.replace('app.css?v=28', 'app.css?v=29')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)
print("Updated index.html to ?v=29")
