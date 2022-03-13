import cv2
import os

folder = "C:/Users/hamza/Desktop/AI/Personal Projects/VGG Implementation/tumor_detection_small/"
images = sorted(os.listdir(folder))
#print(images)
for filename in images:
    imgray = cv2.imread(folder + filename)
    if list(imgray.shape)[2] == 3:
        print(imgray.shape)
        #gray = cv2.cvtColor(imgray, cv2.COLOR_BGR2GRAY)
        #img2 = cv2.merge((gray,gray,gray))
        #cv2.imwrite(folder + filename, img2)