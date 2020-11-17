import cv2
import numpy as np

def sobel_function(source):
    source = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    # source=source.astype(np.float32)

    # sobel_x:发现垂直边缘
    sobel_x = cv2.Sobel(source, cv2.CV_64F, 1, 0)
    # sobel_y:发现水平边缘
    sobel_y = cv2.Sobel(source, cv2.CV_64F, 0, 1)

    sobel_x = np.uint8(np.absolute(sobel_x))
    sobel_y = np.uint8(np.absolute(sobel_y))
    np.set_printoptions(threshold=np.inf)
    # print(sobel_x)

    sum = sobel_x + sobel_y

    return sum
