from PIL import Image
import numpy as np
import os

src = "assets/test/image"
dst = "assets/test/image-parse-v3"

os.makedirs(dst, exist_ok=True)

for f in os.listdir(src):
    if f.endswith(".jpg"):
        img = Image.open(os.path.join(src, f)).convert("L")
        arr = np.array(img)

        # 🔥 KEY FIX: map values to 0–19
        arr = arr % 20

        Image.fromarray(arr.astype('uint8')).save(
            os.path.join(dst, f.replace(".jpg", ".png"))
        )