import face_recognition
import cv2
import os

# Carregar imagens de rostos conhecidos
known_face_encodings = []
known_face_names = []
print('passo0')
for file in os.listdir("imagens"):
    image = face_recognition.load_image_file(f"imagens/{file}")
    encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(encoding)
    known_face_names.append(os.path.splitext(file)[0])
print('passo1')
# Carregar a imagem ou vídeo onde você quer reconhecer os rostos
input_image = face_recognition.load_image_file("Template_Caxias_001.jpg")
input_image = face_recognition.load_image_file("austeclynio_pereira.jpg")
face_locations = face_recognition.face_locations(input_image)
face_encodings = face_recognition.face_encodings(input_image, face_locations)
print('passo2')
# Inicializar o OpenCV para exibir a imagem
#image = cv2.imread("Template_Caxias_001.jpg")
image = cv2.imread("austeclynio_pereira.jpg")

for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Desconhecido"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    # Desenhar um retângulo ao redor do rosto
    cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
    cv2.putText(image, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
    print(name)

# Exibir a imagem com os rostos reconhecidos
cv2.imshow("Reconhecimento Facial", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

