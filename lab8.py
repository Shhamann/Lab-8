import cv2 
import numpy as np 
from matplotlib import pyplot as plt

input_image = cv2.imread('variant-4.jpeg')
b, g, r = cv2.split(input_image)

length, width = input_image.shape[0:2]
for x in range(length):
    for y in range(width):
        g[x, y] = 0
        r[x, y] = 0

merged = cv2.merge([r, g, b])
plt.title('Первое задание')

plt.axis('off')
plt.imshow(merged)
plt.show()