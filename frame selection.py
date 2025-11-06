import os
import random
import shutil
import cv2
import numpy as np

# Folder path
folder_path = r"C:\Users\Osanda\Downloads\NewVideos\codes\New folder\5"

# Get all image files (jpg, png, jpeg)
images = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.png', '.jpeg'))])

# Exclude last 100 frames
if len(images) > 100:
    images = images[:-100]

print(f"Total images considered (excluding last 100): {len(images)}")

# Function to check if an image is blurry using Laplacian variance
def is_blurry(image_path, threshold=100.0):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        return True
    variance = cv2.Laplacian(image, cv2.CV_64F).var()
    return variance < threshold

# Filter out blurry images
non_blurry_images = []
for img_name in images:
    img_path = os.path.join(folder_path, img_name)
    if not is_blurry(img_path):
        non_blurry_images.append(img_name)

print(f"Non-blurry images found: {len(non_blurry_images)}")

# Check if enough clear images exist
if len(non_blurry_images) < 15:
    print(f"Error: Only {len(non_blurry_images)} non-blurry images found. Need at least 15.")
    exit()

# Randomly select 15 non-blurry images
selected_images = random.sample(non_blurry_images, 15)

# Temporary folder to store selected images
temp_folder = os.path.join(folder_path, "selected_temp")
os.makedirs(temp_folder, exist_ok=True)

# Copy and rename selected images
for i, img_name in enumerate(selected_images, start=1):
    src = os.path.join(folder_path, img_name)
    dst = os.path.join(temp_folder, f"{i}.jpg")
    shutil.copy(src, dst)

# Remove old files and move selected ones back
for f in os.listdir(folder_path):
    file_path = os.path.join(folder_path, f)
    if os.path.isfile(file_path):
        os.remove(file_path)

for f in os.listdir(temp_folder):
    shutil.move(os.path.join(temp_folder, f), folder_path)

os.rmdir(temp_folder)

print("✅ 15 high-quality (non-blurry) images selected and renamed from 1.jpg to 15.jpg successfully.")
