import cv2 as cv

# Load two images
img1 = cv.imread('Imagem_Pessoas_Juntas_002.jpg')
#img2 = cv.imread('icons8-opencv-48.png')
img2 = cv.imread('LogoB4H.png')

assert img1 is not None, "file could not be read, check with os.path.exists()"
assert img2 is not None, "file could not be read, check with os.path.exists()"
cv.imshow('Logo',img2)
cv.waitKey(0) 
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
cv.imshow('ROI',roi)
cv.waitKey(0)

# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)

mask_inv = cv.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
 
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:img2.shape[0], 0:img2.shape[1]] = dst
 
cv.imshow('Final',img1)
cv.waitKey(0)
cv.destroyAllWindows()
