import cv2
import numpy as np
img = cv2.imread('modra.jpg', -1)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_modra = np.array([90, 50, 50])
upper_modra = np.array([130, 225, 225])

mask = cv2.inRange(hsv, lower_modra, upper_modra)
#tells us which pixels to keep

result = cv2.bitwise_and(img, img, mask=mask)
#potrebujeme dva sources takze 2 krat img



cv2.imshow('modra', result)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

