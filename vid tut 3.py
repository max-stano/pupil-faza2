import cv2
img = cv2.imread('flower.jpg', -1)
img = cv2.line(img, (0, 0), (300, 300), (255, 0, 0), 100)
img = cv2.line(img, (500, 500), (300, 300), (0, 225, 0), 50)
# source, strating position, ending position, color, line thickness
img = cv2.rectangle(img,(100, 100), (200, 200), (128,128,128), 5)
#source image, center position, radius, color, thickness or -1 to fill

img = cv2.circle(img, (300,300), 70, (0,0,225), -1)
#source image, center position, radius, color, thickness or -1 to fill

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'sussy', (200, 500), font, 4 , (0,0,0), 5, cv2.LINE_AA)
# source image, text displayed, bottom left hand of text, font, font scale, color, hrubka


cv2.imshow('kvetinka', img)
cv2.waitKey()
cv2.destroyAllWindows()
