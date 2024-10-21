import dlib
import cv2


detector = dlib.get_frontal_face_detector()

#image_path = "Grupo_Caxias_001.jpg"
image_path = ("Imagem_Pessoas_Juntas_001.jpg")

image = cv2.imread(image_path)
cv2.imshow('imgPre',image)
cv2.waitKey(0)

faces = detector(image)

for face in faces:
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)


cv2.imshow('imgPos',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
