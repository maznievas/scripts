from PIL import Image

# import os utilities
import os

path = os.path.normpath("/home/someone/Downloads/hands_data/right_hand/")

# define a function that rotates images in the current directory
# given the rotation in degrees as a parameter
def rotateImages(rotationAmt):
  # for each image in the current directory
  for image in os.listdir(path):
    # open the image
    img = Image.open(os.path.join(path, image))
    # rotate and save the image with the same filename
    img.rotate(rotationAmt).save(os.path.join(path, image))
    # close the image
    print('name: ' + image)
    img.close()
    
# examples of use
rotateImages(180)