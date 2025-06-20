import cv2 
import numpy as np 
from matplotlib import pyplot as plt

def task1():
    input_image = cv2.imread('variant-4.jpeg')
    blue_channel = np.array(input_image)
    blue_channel[:, :, 0] = 0 
    blue_channel[:, :, 1] = 0 
    plt.title('Первое задание')
    plt.axis('off')
    plt.imshow(blue_channel)
    plt.show()

def task2():
    

# task1()
task2()