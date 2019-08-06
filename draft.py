import os
from PIL import Image
import glob
#import matplotlib.pyplot as plt 
#import matplotlib.image as img 

os.chdir('C:\Users\maxru_000\Desktop\clash_images')
card_images_list = sorted(glob.glob('C:\Users\maxru_000\Desktop\clash_images'))
images_to_merge = random.choice(card_images_list, k=32)

images = map(Image.open, images_to_merge)
widths, heights = zip(*(i.size for i in images))

total_width = sum(widths)
max_height = max(heights)

new_im = Image.new('RGB', (total_width, max_height))

x_offset = 0
for im in images:
  new_im.paste(im, (x_offset,0))
  x_offset += im.size[0]

new_im.save('test.jpg')

#im = img.imread(images_to_merge)
#plt.imshow(im)
