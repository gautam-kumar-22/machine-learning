import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('Indian-team-photo.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('202667.1.jpg',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

cv2.resize(img, (600, 540))
cv2.imshow('image', img)


cv2.waitKey(0)
cv2.destroyAllWindows()