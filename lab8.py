# вариант 4
import cv2 
import numpy as np 
import time
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
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    i = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, down_points, interpolation=cv2.INTER_LINEAR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        ret, thresh = cv2.threshold(gray, 80, 255, cv2.THRESH_BINARY_INV)

        contours, hierarchy = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            if i % 5 == 0:
                a = x + (w // 2)
                b = y + (h // 2)
                print(f'Центр фигуры: {a, b}')

                #  проверка на попадание метки в область на экране - правая половина
                if x >= down_points[0]//2:
                    print("Вся метка находится в правой половине")
                elif x+w >= down_points[0]//2:
                    print("Часть метки находится в правой половине")

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.1)
        i += 1

    cap.release()


# task1()
task2()