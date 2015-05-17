import numpy as np
import socket
import cv2
 
UDP_IP = "127.0.0.1"
UDP_PORT = 5505
sock = socket.socket(socket.AF_INET, # Internet
			socket.SOCK_DGRAM) # UDP
cap = cv2.VideoCapture(0)

while(True):
	
	# Captura uma imagem e grava no arquivo image.jpg.
	ret, frame = cap.read()
			
	cv2.imwrite('image.jpg',frame)	

	# Le o arquivo image.jpg e manda a informacao em pacotes de 1 K.
	img = open('image.jpg', 'rb') 
	
	data = img.read(1024)
	while (data):
			
    		sock.sendto(data, (UDP_IP, UDP_PORT))

		data = img.read(1024)
	
	# Avisa para o receptor que a transmissao da imagem foi finalizada.
	data = 'end'	
	sock.sendto(data, (UDP_IP, UDP_PORT))

	img.close()

# Quando encerrada a transmissao, libera a camera.
cap.release()

