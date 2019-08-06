import os
from PIL import Image
import glob
#import matplotlib.pyplot as plt 
#import matplotlib.image as img 

os.chdir('C:\Users\maxru_000\Desktop\clash_images')
card_images_list = sorted(glob.glob('C:\Users\maxru_000\Desktop\clash_images'))
images_to_merge = random.choice(card_images_list, k=32)

#im = img.imread(images_to_merge)
#plt.imshow(im)
