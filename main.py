import cv2
import matplotlib.pyplot as plt
img = cv2.imread("flower.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
scaled_image = cv2.resize(rgb_img,(0,0), rgb_img, 0.4, 0.4)

def just_print_for_all(event, x, y, flags, param):
    print("chercher tech is my name")

# set when to have a call back
cv2.namedWindow("Title of Popup Window")

#what to happen on call back
cv2.setMouseCallback("Title of Popup Window", just_print_for_all)

#show image to user with title
cv2.imshow("Title of Popup Window", scaled_image)
cv2.waitKey()
cv2.destroyAllWindows()


