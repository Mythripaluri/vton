import os
from PIL import Image
import numpy as np

# Create image-parse-agnostic-v3.2 folder
dst = "assets/test/image-parse-agnostic-v3.2"
os.makedirs(dst, exist_ok=True)

# Create placeholder parse maps (semantic segmentation)
# Parse maps use semantic indices in range [0, 19]
# Valid indices: 0=background, 1=body, 2-19=clothing/accessories
width, height = 512, 512  # Standard size for the model

# Create various patterns using valid semantic indices (0-19)
patterns = [
    lambda h, w: np.full((h, w), 0, dtype=np.uint8),  # person1: all background
    lambda h, w: np.full((h, w), 1, dtype=np.uint8),  # person2: all body
    lambda h, w: np.full((h, w), 5, dtype=np.uint8),  # person3: all clothing type 5
    lambda h, w: np.ones((h, w), dtype=np.uint8) * (np.arange(h)[:, np.newaxis] % 20),  # person4: gradient 0-19
    lambda h, w: np.ones((h, w), dtype=np.uint8) * (np.arange(w) % 20),  # person5: horizontal gradient
    lambda h, w: np.random.randint(0, 20, (h, w), dtype=np.uint8),  # person6: random indices 0-19
]

for i in range(1, 7):
    person_name = f"person{i}"
    img_file = os.path.join(dst, f"{person_name}.png")
    
    # Generate parse map using pattern
    parse_map = patterns[i-1](height, width)
    img = Image.fromarray(parse_map, mode='L')
    img.save(img_file)
    print(f"✅ Created {person_name}.png")

print("✅ All parse agnostic maps created!")
