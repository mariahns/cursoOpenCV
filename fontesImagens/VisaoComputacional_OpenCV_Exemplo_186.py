import numpy as np
import cv2
azulEscuro = np.array([100, 67, 0], dtype = "uint8")
azulClaro = np.array([255, 128, 50], dtype = "uint8")


camera = cv2.VideoCapture('Video_Curso_004.mp4')
while True:
    (sucesso, frame) = camera.read()
    if not sucesso:
        break
    obj = cv2.inRange(frame,azulEscuro, azulClaro)    
    obj = cv2.GaussianBlur(obj, (3, 3), 0)    
    cnts,hierarchy = cv2.findContours(obj.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) > 0:
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 255), 1)
        cv2.imshow("Tracking", frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
camera.release()
cv2.destroyAllWindows()
