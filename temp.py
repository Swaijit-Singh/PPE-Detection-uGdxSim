import os
import shutil
# import imgaug.augmenters as iaa

# directory = r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim'
# os.chdir(directory)

# IMG = cv2.imread(
#     r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim\images_main\maksssksksss0.png')
# cv2.imshow("Masks", IMG)

# augmentation_pipeline = iaa.Sequential([
#     # iaa.ChangeColorspace(from_colorspace="BGR", to_colorspace="RGB"),
#     iaa.AddToHueAndSaturation((-50, 50), per_channel=True),
#     # iaa.ChangeColorspace(from_colorspace="RGB", to_colorspace="BGR")
# ])

# augmented_img = augmentation_pipeline(image=IMG)
# cv2.imshow("AUGMENTED", augmented_img)

# filename = 'AUGMENTATION_TEST.png'
# cv2.imwrite(filename, augmented_img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
# xml_dir = r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim\annotations'
# new_xml_path = r'C:\Users\musta\OneDrive\Desktop\Simulanis_Internship\PPE-Detection-uGdxSim\Augmented_images\annotation_aug'

# for xmlfilename in os.listdir(xml_dir):
#     if xmlfilename.endswith(".xml"):
#         new_xml_filename = xmlfilename.replace(".xml", "_04.xml")
#         new_xml_path = os.path.join(new_xml_path, new_xml_filename)
#         shutil.copy(xml_dir, new_xml_path)


import shutil
import os
