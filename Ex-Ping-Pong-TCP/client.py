#client.py

#!/usr/bin/python                               # This is client.py file

import socket                                   # Import socket module

s = socket.socket()                             # Create a socket object
host = socket.gethostname()                     # Get local machine name
port = 12345                                    # Reserve a port for your service.

print('conectando-se ao servidor')
s.connect((host, port))
print('Conectado')
msg = 'msg'

while (True):
    msg = input('Digite mensagem: ')
    s.send(msg.encode())
    if (msg == 'SAIR'):
        break    
    print('Mensagem enviada\nEsperando resposta')
    data = s.recv(4096)
    print('Resposta recebida: ' + data.decode())
print('Desconectando.')
s.close()                                         # Close the socket when done