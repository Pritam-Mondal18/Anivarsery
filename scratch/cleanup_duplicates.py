import os

files_to_delete = [
    # Root duplicate/unused video files
    r"prevdo.mp4",
    r"vdo.mp4",
    r"vdo1.mp4",
    r"vdo2.mp4",
    r"inspect_card_fe.py",
    # Unused video files in assets/
    os.path.join("assets", "hero-tall.mp4"),
    os.path.join("assets", "hero-wide.mp4"),
    # Unused video files in public/assets/
    os.path.join("public", "assets", "hero-tall.mp4"),
    os.path.join("public", "assets", "hero-wide.mp4"),
    os.path.join("public", "assets", "vdo.mp4"),
    os.path.join("public", "assets", "vdo1.mp4"),
]

total_freed = 0
deleted_count = 0

for f in files_to_delete:
    if os.path.exists(f):
        size = os.path.getsize(f)
        try:
            os.remove(f)
            total_freed += size
            deleted_count += 1
            print(f"Deleted: {f} ({size / (1024*1024):.2f} MB)")
        except Exception as e:
            print(f"Error deleting {f}: {e}")
    else:
        print(f"File not found (already deleted): {f}")

print(f"\nTotal deleted: {deleted_count} files, {total_freed / (1024*1024):.2f} MB freed.")
