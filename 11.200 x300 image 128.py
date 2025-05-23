import numpy as np

# Create a 200x300 array filled with 128 (grayscale value)
img = np.full((200, 300), 128, dtype=np.uint8)

print(img.shape)  # (200, 300)
print(img)