#server.py
#!/usr/bin/python                               # This is server.py file

import socket                                   # Import socket module

s = socket.socket()                             # Create a socket object
host = socket.gethostname()                     # Get local machine name
port = 12345                                    # Reserve a port for your service.
s.bind((host, port))                            # Bind to the port

s.listen(5)                                     # Now wait for client connections.
while True:
   print('Esperando conexão.')
   c, addr = s.accept()                         # Establish connection with client.
   print('Conectado')
   while(True):
      print('Esperando mensagem')
      data = c.recv(4096)
      if (data.decode() == 'SAIR'):
         print('Conexão encerrada.')
         break
      print('Mensagem recebida: ' + data.decode())
      resp = input('Digite resposta: ')
      c.send(resp.encode())
      print('Resposta enviada.')
   c.close()                                    # Close the connection