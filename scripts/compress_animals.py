import os
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent / "images" / "webp" / "animals"
MAX_SIDE = 1600
QUALITY = 82

total_before = 0
total_after = 0

for webp in ROOT.rglob("*.webp"):
    before = webp.stat().st_size
    total_before += before
    img = Image.open(webp)
    w, h = img.size
    scale = min(1.0, MAX_SIDE / max(w, h))
    if scale < 1.0:
        new_size = (int(w * scale), int(h * scale))
        img = img.resize(new_size, Image.LANCZOS)
    img.save(webp, "WEBP", quality=QUALITY, method=6)
    after = webp.stat().st_size
    total_after += after
    print(f"{webp.relative_to(ROOT.parent.parent.parent)}: {before/1024:.0f}KB -> {after/1024:.0f}KB ({100*after/before:.0f}%)")

print(f"\nTOTAL: {total_before/1024/1024:.2f}MB -> {total_after/1024/1024:.2f}MB ({100*total_after/total_before:.0f}%)")
