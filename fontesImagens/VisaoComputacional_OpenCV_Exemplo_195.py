import cv2
import numpy as np

# Função para detectar a cor amarela
def detect_yellow(image_path):
    # Carregar a imagem
    image = cv2.imread(image_path)
    
    # Converter a imagem para o espaço de cor HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Definir o intervalo de cor para amarelo
    lower_yellow = np.array([23, 93, 0])  # Intervalo inferior do amarelo
    upper_yellow = np.array([45, 255, 255])  # Intervalo superior do amarelo
    
    # Criar a máscara para a cor amarela
    yellow_mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    
    # Aplicar a máscara na imagem original
    yellow_result = cv2.bitwise_and(image, image, mask=yellow_mask)

    # Mostrar os resultados
    cv2.imshow('Original Image', image)
    cv2.waitKey(0)
    cv2.imshow('Yellow Mask', yellow_mask)
    cv2.waitKey(0)
    cv2.imshow('Detected Yellow Color', yellow_result)
    cv2.waitKey(0)
    
    # Esperar até que uma tecla seja pressionada e fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Caminho da imagem
image_path = 'Imagens_Figuras_Geometricas_001.jpg'

# Detectar a cor amarela
detect_yellow(image_path)
