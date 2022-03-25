import cv2
img = cv2.imread('flower.jpg', 0)
# cv2.IMREAD_UNCHANGED - transparencia zanedbana = 1
# cv2.IMREAD_GRAYSCALE - čiernobiely obrazok = 0
# cv2.IMREAD_COLOR - color image = -1#
img = cv2.resize(img, (400, 400))
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('new_img.jpg', img)
cv2.imshow('kvetinka', img)
cv2.waitKey()
cv2.destroyAllWindows()