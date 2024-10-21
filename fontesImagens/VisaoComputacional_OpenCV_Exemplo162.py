import cv2
import numpy as np
import math
img = cv2.imread('Imagem_Raio_001.jpg',1)
img1 = cv2.imread('Imagem_Raio_001.jpg',cv2.IMREAD_GRAYSCALE)
assert img1 is not None, "file could not be read, check with os.path.exists()"


ret,thresh = cv2.threshold(img1,127,255,0)
contours,hierarchy = cv2.findContours(thresh, 1, 2)
 
cnt = contours[0]
x,y,w,h = cv2.boundingRect(cnt)
img2= cv2.rectangle(img.copy(),(x,y),(x+w,y+h),(0,255,0),2)
perimetro = cv2.arcLength(cnt,True)
print(math.trunc(perimetro))

cv2.imshow("Image", img2)
cv2.waitKey(0)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.intp(box)
cv2.drawContours(img,[box],0,(0,0,255),2)

perimetro = cv2.arcLength(box,True)
print(math.trunc(perimetro))

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
