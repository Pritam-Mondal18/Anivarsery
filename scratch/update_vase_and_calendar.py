import os
import re

# 1. Update JS files to remove calBtn
def update_js(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    target = 'c.jsxs("a", { className: "btn btn--crimson scratch__cal", id: "calBtn", target: "_blank", rel: "noopener", children: [c.jsx("svg", { children: c.jsx("use", { href: "#i-cal" }) }), "Add to calendar"] })'
    if target in content:
        content = content.replace(target, 'null')
        print(f"Removed calBtn from {filepath}")
    else:
        print(f"Warning: target not found in {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_js('assets/app.js')
update_js('public/assets/app.js')

# 2. Update CSS files for vase position and calBtn hiding
def update_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace bottom:0 for .vase
    if '.vase{position:absolute;bottom:0;' in content:
        content = content.replace('.vase{position:absolute;bottom:0;', '.vase{position:absolute;bottom:clamp(60px,7vw,100px);')
        print(f"Updated .vase bottom in {filepath}")
    else:
        print(f"Warning: .vase bottom:0 not found in {filepath}")

    # Mobile override
    if '.vase{width:70px}' in content:
        content = content.replace('.vase{width:70px}', '.vase{width:70px;bottom:40px}')
        print(f"Updated mobile .vase in {filepath}")

    # Ensure #calBtn is hidden
    hide_rule = '\n#calBtn,.scratch__cal{display:none!important;visibility:hidden!important;height:0!important;margin:0!important;padding:0!important;pointer-events:none!important;}\n'
    if '#calBtn' not in content:
        content += hide_rule
        print(f"Added #calBtn hide rule to {filepath}")

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_css('assets/app.css')
update_css('public/assets/app.css')

# 3. Update index.html cache bust version to v=32
with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

idx = re.sub(r'app\.js\?v=\d+', 'app.js?v=32', idx)
idx = re.sub(r'app\.css\?v=\d+', 'app.css?v=32', idx)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)
print("Updated index.html to ?v=32")
