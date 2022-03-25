import cv2
#import random
img = cv2.imread('flower.jpg', -1)
#1 print(img.shape) - height x width x channel (color arrays - bgr)
#2 print(img[0][45:60]) ukaze prvy radiok specificky pixely od 45 po 60
#3 for i in range(100): #looping through the firt 100 rows
    #for j in range(img.shape[1]): #aby to prešlo celou šírkou obrazku
        #img [i][j] = [random.randint(0,225),random.randint(0,225),random.randint(0,225)]
#nahradzame prvych 100 riadkov úpixelv nahradnou farbou - 3 randitn kvoli rgb

#4tag = img[100:200, 300:400] #copy rows od 500 do 700 columns  600ay 900
#4img[300:400, 100:200] = tag #slice image array nahradime tag sliceom



cv2.imshow('kvietok', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
