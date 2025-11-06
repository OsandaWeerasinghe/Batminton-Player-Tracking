import os
import shutil

# Main folder containing subfolders 1 to 5
main_folder = r"C:\Users\Osanda\Downloads\NewVideos\codes\New folder"

# Output folder where all images will be copied
output_folder = os.path.join(main_folder, "All_Images")

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Loop through each subfolder (1 to 5)
for i in range(1, 6):
    subfolder_path = os.path.join(main_folder, str(i))
    
    if not os.path.exists(subfolder_path):
        print(f"Subfolder {subfolder_path} not found.")
        continue
    
    # Get all image files (jpg, png, jpeg)
    images = [f for f in os.listdir(subfolder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    for img_name in images:
        src = os.path.join(subfolder_path, img_name)
        # Rename to avoid overwriting if same names exist
        new_name = f"{i}_{img_name}"
        dst = os.path.join(output_folder, new_name)
        shutil.copy(src, dst)

print("✅ All images copied successfully to:", output_folder)
