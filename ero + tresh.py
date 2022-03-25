import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('pupil.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
img = cv.medianBlur(img, 5)
img = cv2.erode(img, kernel, iterations=1)
edges = cv.Canny(img,100,200)

plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.show()

#cv2.imshow('', img)
#cv2.waitKey()
#cv2.destroyAllWindows()

