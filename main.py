from PIL import Image
import os

input_folder = "images"      # Folder containing PNG files
output_folder = "webP"    # Folder for WebP files

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        png_path = os.path.join(input_folder, filename)

        # Remove .png extension and add .webp
        webp_filename = os.path.splitext(filename)[0] + ".webp"
        webp_path = os.path.join(output_folder, webp_filename)

        try:
            img = Image.open(png_path)

            # Convert RGBA images properly
            img.save(webp_path, "WEBP", quality=80)

            print(f"Converted: {filename} -> {webp_filename}")

        except Exception as e:
            print(f"Error converting {filename}: {e}")

print("Conversion completed!")
