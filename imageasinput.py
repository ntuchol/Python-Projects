from PIL import Image

def process_image(image_path):
    try:
        img = Image.open(image_path)
        
        print(f"Image Format: {img.format}")
        print(f"Image Size: {img.size}")
        print(f"Image Mode: {img.mode}")
        
        img.show()
    except FileNotFoundError:
        print("Error: The specified image file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

image_path = input("Enter the path to your image file: ")
process_image(image_path)


