import io
import os
from PIL import Image

for fname in ['h12.NEF', 'h17.NEF']:
    fp = os.path.join('public', 'gayeholud', fname)
    with open(fp, 'rb') as f:
        data = f.read()

    pos = 0
    best_img = None
    best_size = 0
    while True:
        idx = data.find(b'\xff\xd8\xff', pos)
        if idx == -1:
            break
        end_idx = data.find(b'\xff\xd9', idx)
        if end_idx != -1:
            raw_jpg = data[idx:end_idx+2]
            try:
                im = Image.open(io.BytesIO(raw_jpg))
                if im.size[0] * im.size[1] > best_size:
                    best_size = im.size[0] * im.size[1]
                    best_img = (raw_jpg, im.size)
            except Exception:
                pass
            pos = end_idx + 2
        else:
            pos = idx + 3

    if best_img:
        print(f'{fname}: largest JPEG dims = {best_img[1]}')
        out_name = os.path.join('public', 'gayeholud', fname[:-4] + '.JPG')
        with open(out_name, 'wb') as out_f:
            out_f.write(best_img[0])
        print(f'Saved as {out_name}')
