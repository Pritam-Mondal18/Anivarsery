with open('assets/app.js', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('eventGalleriesData')
idx2 = text.find('"event-biye"', idx)
print(text[idx2:idx2+600])
