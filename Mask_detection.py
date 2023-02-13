import cv2 as cv
import os

dir_path = r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim\resized_images_main'

# Load the cascade classifier
face_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
mask_cascade = cv.CascadeClassifier("haarcascade_mask.xml")

# Define the desired size of the resized image
desired_size = (224, 224)

# Loop over all the images in the directory
for filename in os.listdir(dir_path):

    # Load the image
    img = cv.imread(os.path.join(dir_path, filename))

    # # Resize the image to the desired size
    # img = cv.resize(img, desired_size)

    # Convert the image to grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Loop over the faces
    for (x, y, w, h) in faces:
        # Crop the face region
        face_roi = gray[y:y+h, x:x+w]

        # Detect masks in the face region
        masks = mask_cascade.detectMultiScale(
            face_roi, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangles around the masks
        for (mask_x, mask_y, mask_w, mask_h) in masks:
            cv.rectangle(img, (x+mask_x, y+mask_y), (x+mask_x +
                                                     mask_w, y+mask_y+mask_h), (0, 255, 0), 2)

    # Show the original image with rectangles around the masks
    cv.imshow("Masks", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
