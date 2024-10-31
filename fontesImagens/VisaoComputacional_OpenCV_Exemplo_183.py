import cv2
def redim(img, largura): #função para redimensionar uma imagem
 alt = int(img.shape[0]/img.shape[1]*largura)
 img = cv2.resize(img, (largura, alt), interpolation = cv2.INTER_AREA)
 return img

df = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)
while True: 
    (sucesso, frame) = camera.read()
    if not sucesso: #final do vídeo
        break
    frame = redim(frame,1280) 
    frame_pb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = df.detectMultiScale(frame_pb, 1.3,2)
    frame_temp = frame.copy()
    for (x, y, lar, alt) in faces:
        cv2.rectangle(frame_temp, (x, y), (x + lar, y + alt), (0,255, 255), 3)
        cv2.imshow("Procurando faces.....", redim(frame_temp, 640))
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break
camera.release()
cv2.destroyAllWindows()
