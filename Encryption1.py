import os
from PIL import Image


def encrypt_image(image_path, output_path, key):
    # Open the image
    image = Image.open(image_path)

    # Convert to RGB if the image has transparency (alpha channel)
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    pixels = image.load()  # Load pixel data
    width, height = image.size

    # Encrypt each pixel
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (r ^ key, g ^ key, b ^ key)

    # Save the encrypted image
    image.save(output_path)
    print(f"Encrypted image saved at: {output_path}")


def main():
    # Path to your folder with images to encrypt
    image_folder = r"C:\Users\mihad\Documents\encrypt"
    # Where you want to save the encrypted images
    output_folder = r"C:\Users\mihad\Pictures\encrypt"
    key = 123  # Example encryption key

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Go through each file in the folder
    for filename in os.listdir(image_folder):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(image_folder, filename)
            output_path = os.path.join(output_folder, f"encrypted_{filename}")
            encrypt_image(image_path, output_path, key)


if __name__ == "__main__":
    main()
