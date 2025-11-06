import os

# Folder containing the .jpg files
folder_path = r"C:\Users\Osanda\Downloads\NewVideos\codes\New folder\All_Images"

# Get all .jpg files
files = [f for f in os.listdir(folder_path) if f.lower().endswith('.jpg')]

# Sort files to ensure proper order
files.sort()

# Rename files sequentially from 1.jpg to 141.jpg
for i, filename in enumerate(files, start=1):
    old_path = os.path.join(folder_path, filename)
    new_filename = f"{i}.jpg"
    new_path = os.path.join(folder_path, new_filename)
    os.rename(old_path, new_path)
    print(f"Renamed: {filename} → {new_filename}")

print("✅ All JPG files renamed successfully from 1.jpg to 141.jpg!")
