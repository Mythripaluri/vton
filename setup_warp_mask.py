import os
import shutil

pairs = [
    ("person1.jpg", "cloth1.jpg"),
    ("person2.jpg", "cloth2.jpg"),
    ("person3.jpg", "cloth3.jpg"),
    ("person4.jpg", "cloth4.jpg"),
    ("person5.jpg", "cloth5.jpg"),
    ("person6.jpg", "cloth6.jpg"),
]

src = "assets/test/cloth-mask"
dst = "assets/test/cloth-warp-mask"

os.makedirs(dst, exist_ok=True)

for person, cloth in pairs:
    shutil.copy(
        os.path.join(src, cloth),
        os.path.join(dst, person)  # rename to person
    )

print("✅ All warped cloth-mask files created!")
