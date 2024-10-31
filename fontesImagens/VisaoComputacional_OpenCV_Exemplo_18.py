import cv2 as cv
cam = cv.VideoCapture(0)

if not cam.isOpened():
 print("Error opening camera")
 exit()
while True:
 # Capture frame-by-frame
 ret, frame = cam.read()
 # if frame is read correctly ret is True
 if not ret:
     print("Error in retrieving frame")
     break
 cv.imshow('Que Horror!', frame)
 
 
# Press 'q' to quit
 if cv.waitKey(10)== ord('q'): 
     break
cam.release()
cv.destroyAllWindows()
