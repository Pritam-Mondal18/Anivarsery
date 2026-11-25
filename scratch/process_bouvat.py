import os
from PIL import Image, ImageOps

src_dir = os.path.join('assets', 'bouvat')
out_assets_dir = os.path.join('assets', 'bouvat')
out_public_assets_dir = os.path.join('public', 'assets', 'bouvat')

os.makedirs(out_public_assets_dir, exist_ok=True)

results = []

for i in range(1, 25):
    fname = f'r{i}.JPG'
    fp = os.path.join(src_dir, fname)
    if not os.path.exists(fp):
        print(f"Warning: {fname} missing")
        continue

    with Image.open(fp) as img:
        img = ImageOps.exif_transpose(img)
        w, h = img.size
        # Resize to max dim 1600
        max_dim = 1600
        if max(w, h) > max_dim:
            if w > h:
                new_w = max_dim
                new_h = int(h * (max_dim / w))
            else:
                new_h = max_dim
                new_w = int(w * (max_dim / h))
            resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
        else:
            resized = img
            new_w, new_h = w, h

        out_name = f'bv{i}.jpeg'
        out_p1 = os.path.join(out_assets_dir, out_name)
        out_p2 = os.path.join(out_public_assets_dir, out_name)

        resized.save(out_p1, 'JPEG', quality=88, optimize=True)
        resized.save(out_p2, 'JPEG', quality=88, optimize=True)

        size_kb = os.path.getsize(out_p1) / 1024
        orient = "Landscape" if new_w > new_h else "Portrait"
        results.append((i, fname, out_name, new_w, new_h, orient, size_kb))
        print(f"{fname} -> {out_name}: {new_w}x{new_h} ({orient}), {size_kb:.1f} KB")

print(f"Total processed: {len(results)}")
