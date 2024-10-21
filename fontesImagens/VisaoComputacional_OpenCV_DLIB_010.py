import face_recognition
import cv2

# Carregar a imagem
image = face_recognition.load_image_file("Grupo_Caxias_001.jpg")

# Encontrar todas as faces na imagem e fazer o encoding
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

# Carregar imagens de referência e aprender a reconhecer
known_image = face_recognition.load_image_file("Template_Caxias_001.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

# Iniciar variáveis
known_encodings = [known_encoding]
known_names = ["Paulo Cientista"]

# Carregar a imagem usando OpenCV para desenhar retângulos
image_cv = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Reconhecer faces na imagem
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_encodings, face_encoding)
    name = "?"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_names[first_match_index]

    # Desenhar retângulo ao redor da face e adicionar o nome
    cv2.rectangle(image_cv, (left, top), (right, bottom), (0, 255, 0), 2)
    cv2.putText(image_cv, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Mostrar a imagem com as faces reconhecidas
cv2.imshow("Faces reconhecidas", image_cv)
cv2.waitKey(0)
cv2.destroyAllWindows()
