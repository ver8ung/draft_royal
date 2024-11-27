import random
from PIL import Image

# Define a list of image file paths to use
image_paths = ["path/to/image1.png", "path/to/image2.png", "path/to/image3.png"]

# Function to load a random image
def load_random_image():
    # Choose a random image path from the list
    image_path = random.choice(image_paths)
    
    # Load the image
    img = Image.open(image_path)
    
    return img

# Generate a set of random images
num_images = 5
images = [load_random_image() for _ in range(num_images)]

# Save the images to files
for i, img in enumerate(images):
    img.save(f"random_image_{i+1}.png")

print(f"{num_images} random images have been generated and saved as 'random_image_1.png' to 'random_image_{num_images}.png'.")
