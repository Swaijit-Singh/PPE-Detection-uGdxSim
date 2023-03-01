import os
import cv2
import shutil
from imgaug import augmenters as iaa

# define the input and output directories
input_dir = r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim\images_main'
output_dir = r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim\Augmented_images'

# define the image augmentation pipeline
augmentation_pipeline = iaa.Sequential([
    # CODE= ._00 # 0.0 is fully color and 1.0 is fully grey
    # iaa.Grayscale(alpha=(0.0, 1.0)),

    # CODE= ._01 # 1000-4000 is warm and 10000-40000 is cold
    iaa.ChangeColorTemperature((1000, 4000))

    # CODE= ._02 # 0.5 is 50% of all pixels are inverted
    # iaa.Invert(0.5),

    # CODE= ._03 # inc or dec brightness by a factor
    # iaa.MultiplyBrightness((0.5, 1.5)),

    # CODE= ._04 # 50% of hue and saturation in RGB is changed
    # iaa.AddToHueAndSaturation((-50, 50), per_channel=True),
])

# loop through each image file in the input directory
for filename in os.listdir(input_dir):

    # check if the file is an image
    if filename.endswith(".png"):

        # load the image
        img_path = os.path.join(input_dir, filename)
        img = cv2.imread(img_path)

        # apply the image augmentation pipeline
        augmented_img = augmentation_pipeline(image=img)

        # get the new filename and path for the augmented image
        new_filename = filename.replace(".png", "_01.png")
        new_img_path = os.path.join(output_dir, new_filename)

        # save the augmented image and copy the original XML file to the new location
        cv2.imwrite(new_img_path, augmented_img)


src_dir = r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim\annotations'
dst_dir = r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim\Augmented_images\annotation_aug'

# loop through all files in the source directory
for xmlfilename in os.listdir(src_dir):
    if xmlfilename.endswith('.xml'):
        # set the source and destination paths
        src_path = os.path.join(src_dir, xmlfilename)
        dst_path = os.path.join(dst_dir, xmlfilename)

        # copy the file from source to destination
        shutil.copy(src_path, dst_path)

        # rename the file in the destination folder
        new_name = xmlfilename.replace('.xml', '_01.xml')
        os.rename(os.path.join(dst_dir, xmlfilename),
                  os.path.join(dst_dir, new_name))
