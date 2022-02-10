from http.client import PROXY_AUTHENTICATION_REQUIRED
from itertools import permutations
import socket
import sys

mi_socket = socket.socket()
mi_socket.connect(('localhost',8000))

while True:
    mensaje = input()
    if mensaje != 'terminar':
        mi_socket.send(mensaje.encode())
        respuesta = mi_socket.recv(4096).decode()
        print(respuesta)
    else:
        mi_socket.send(mensaje.encode())
        mi_socket.close()
        sys.exit()
