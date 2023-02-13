import cv2 as cv
import os

# Define the desired image size
width = 224
height = 224

# Get a list of all the image files in the folder
folder = r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim\images_main'
resized_path = r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim\resized_images_main'

files = [f for f in os.listdir(folder) if f.endswith('.png')]
print(files)

# Loop over the image files
for file in files:
    # Load the image
    img = cv.imread(os.path.join(folder, file))

    # Resize the image
    resized_img = cv.resize(img, (width, height), cv.INTER_LINEAR)

    # Save the resized image
    cv.imwrite(os.path.join(resized_path, 'resized_' + file), resized_img)
