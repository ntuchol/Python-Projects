Here’s a simple Python program that takes an image as input and performs basic operations like displaying it. This example uses the popular Pillow library for image processing.

Copy the code
from PIL import Image

# Function to load and display an image
def process_image(image_path):
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Display image details
        print(f"Image Format: {img.format}")
        print(f"Image Size: {img.size}")
        print(f"Image Mode: {img.mode}")
        
        # Show the image
        img.show()
    except FileNotFoundError:
        print("Error: The specified image file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input: Path to the image file
image_path = input("Enter the path to your image file: ")
process_image(image_path)

How It Works:
Input: The program prompts the user to enter the path to the image file.
Processing: It uses the Pillow library to open and process the image.
Output: Displays the image's format, size, and mode, and opens the image in the default viewer.
Notes:
Install the Pillow library if you don’t already have it by running:
Copy the code
pip install pillow

Ensure the image file path is correct and accessible.

This program can be extended to perform additional operations like resizing, cropping, or applying filters. Let me know if you'd like to explore those!
