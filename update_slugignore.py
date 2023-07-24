import os
import random

folder_path = "inputs/malaria_dataset/cell_images/validation"

# Initialize a list to store image paths from both subfolders
image_files = []

# Iterate through the subfolders
for subfolder in os.listdir(folder_path):
    subfolder_path = os.path.join(folder_path, subfolder)
    # Get a list of all image files in the subfolder
    images_in_subfolder = [file for file in os.listdir(
        subfolder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    # Append the image paths to the main list
    image_files.extend([os.path.join(subfolder_path, image)
                       for image in images_in_subfolder])

# Calculate the number of images to add to .slugignore (1/3 of the total images)
num_images_to_ignore = len(image_files) // 3

# Select random images to add to .slugignore
images_to_ignore = random.sample(image_files, num_images_to_ignore)

# Open .slugignore file and append the selected image paths
with open(".slugignore", "a") as file:
    for image in images_to_ignore:
        file.write(f"{image}\n")

print(f"{num_images_to_ignore} images added to .slugignore.")


def add_images_to_slugignore(folder_path, num_images_to_ignore):
    image_files = [file for file in os.listdir(
        folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]
    images_to_ignore = random.sample(image_files, num_images_to_ignore)
    with open(".slugignore", "a") as file:
        for image in images_to_ignore:
            file.write(f"{os.path.join(folder_path, image)}\n")


# Folder paths for Parasitized and Uninfected folders
parasitized_folder_path = "inputs/malaria_dataset/cell_images/Parasitized"
uninfected_folder_path = "inputs/malaria_dataset/cell_images/Uninfected"

# Calculate the number of images to add to .slugignore (1/10 of the total images in each folder)
num_images_to_ignore_parasitized = len(
    os.listdir(parasitized_folder_path)) // 10
num_images_to_ignore_uninfected = len(os.listdir(uninfected_folder_path)) // 10

# Add random images from both folders to .slugignore
add_images_to_slugignore(parasitized_folder_path,
                         num_images_to_ignore_parasitized)
add_images_to_slugignore(uninfected_folder_path,
                         num_images_to_ignore_uninfected)

print(f"{num_images_to_ignore_parasitized} images added to .slugignore from Parasitized folder.")
print(f"{num_images_to_ignore_uninfected} images added to .slugignore from Uninfected folder.")
