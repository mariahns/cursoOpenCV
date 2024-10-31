import cv2 
import numpy as np
import math
  
# Load the image 
image = cv2.imread('Varios_Parafusos_Diferentes_002.jpg')

assert image is not None, "file could not be read, check with os.path.exists()"
cv2.imshow('Original', image)
cv2.waitKey(0)
  
# Convert the image to grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)
  
blur = cv2.bilateralFilter(src=gray, d=9, sigmaColor=75, sigmaSpace=75)
ret, thresh2 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('threshold', thresh2)
cv2.waitKey(0)

  
# Find the contours of the objects in the image 
contours, hierarchy = cv2.findContours(thresh2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Objetos na imagem : ", len(contours))
  
# Loop through the contours and calculate the perimeter of each object 
cont = 0
for cnt in contours:
    cont = cont + 1
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.intp(box)
    cv2.drawContours(image,[box],0,(0,0,255),2)
    perimetro = cv2.arcLength(box,True)

    teste = "Fora do padrao"
    if perimetro>=180 and perimetro<=200 :
        teste = "Padrao"    
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.putText(image, str(cont) + "-" + str(math.trunc(perimetro)),(x, y),cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)
    print(f"Objeto numero {cont}  : {teste}") 
 
# Show the final image  
cv2.imshow('image', image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
