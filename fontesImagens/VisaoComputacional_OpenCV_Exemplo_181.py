import cv2

def redim(img, largura): #função para redimensionar uma imagem
 alt = int(img.shape[0]/img.shape[1]*largura)
 img = cv2.resize(img, (largura, alt), interpolation = cv2.INTER_AREA)
 return img

from ffpyplayer.player import MediaPlayer

file="Video_Curso_002.mp4"
video=cv2.VideoCapture(file)
player = MediaPlayer(file)
while True:
 ret, frame=video.read()
 audio_frame, val = player.get_frame()
 if not ret:
     print("End of video")
     break
 cv2.waitKey(20)
 
 cv2.imshow("Video", redim(frame,1280))
 if val != 'eof' and audio_frame is not None:
 #audio
     img, t = audio_frame
video.release()
cv2.destroyAllWindows()
