import cv2 as cv

img1 = cv.imread('night_sky.jpg')
img2 = cv.imread('moon.jpg')


img2 = cv.resize(img2, None, fx = 0.5, fy = 0.5)
cv.imshow('IMG1',img1)
cv.waitKey(0)
cv.imshow('IMG2',img2)
cv.waitKey(0)

img_2_shape = img2.shape
roi = img1[0:img_2_shape[0],0:img_2_shape[1]]
cv.imshow('ROI',roi)
cv.waitKey(0)

img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)

ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
cv.imshow('Mask',mask)
cv.waitKey(0)

mask_inv = cv.bitwise_not(mask)
cv.imshow('Mask Invertida',mask_inv)
cv.waitKey(0)

# Now black-out the area of moon in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
cv.imshow('IMG1_bg',img1_bg)
cv.waitKey(0)

# Take only region of moon from moon image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
cv.imshow('img2_fg',img2_fg)
cv.waitKey(0) 
# Put moon in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:img_2_shape[0], 0:img_2_shape[1]] = dst

#Create resizable windows for our display images
cv.imshow('img2_fg',img2_fg)
cv.waitKey(0)
cv.imshow('Imagem Final',img1)
cv.waitKey(0)
cv.destroyAllWindows()
