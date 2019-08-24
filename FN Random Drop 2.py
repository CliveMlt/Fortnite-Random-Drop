import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
from random import seed
from random import randint

for _ in range(1750):
	valuex = randint(0, 1750)

for _ in range(1790):
	valuey = randint(0, 1790)

im = np.array(Image.open('map5.png'), dtype=np.uint8)
fig,ax = plt.subplots(1)
ax.imshow(im)
rect = patches.Ellipse((valuex,valuey),110,90,linewidth=2,edgecolor='r',facecolor='none')
ax.add_patch(rect)
plt.show()