import numpy as np
import socket
import cv2
 
UDP_IP = "127.0.0.1"
UDP_PORT = 5505
sock = socket.socket(socket.AF_INET, # Internet
				socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while(True):

	img = open('img.jpg', 'wb') # Cria um arquivo .jpg

	data, addr = sock.recvfrom(1024) # recebe pacote com paylod de 1 K
	
	# Enquanto nao receber a confirmacao de que a transmissao foi encerrada grava a informacao no arquivo .jpg.
	while (data  != 'end'):

		img.write(data)
		img.flush()
				
		data, addr = sock.recvfrom(1024)
		
	
	# Fecha o arquivo .jpg
	img.close()

	# Tenta abrir a imagem recebida	e caso ela tenha sido corrompida mostra a mensagem de erro.
	try:
		
		# Carrega a imagem.
		image = cv2.imread('img.jpg',cv2.IMREAD_COLOR)
	
		# Cria uma janela para a visualizacao da imagem recebida.
		cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
		cv2.imshow('frame',image)
		
	except cv2.error as e:
		
		print ("Imagem corrompida.")


	
    	# Caso a tecla q seja pressionada encerra o programa.
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# Destroi as janelas abertas pelo openCV.
cv2.destroyAllWindows()

