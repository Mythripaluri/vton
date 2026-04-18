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

src = "assets/test/cloth"
dst = "assets/test/cloth-warp"

os.makedirs(dst, exist_ok=True)

for person, cloth in pairs:
    src_path = os.path.join(src, cloth)
    dst_path = os.path.join(dst, person)
    print(f"Copying {cloth} -> {person}")
    shutil.copy(src_path, dst_path)

print("✅ All warped cloth files created!")
