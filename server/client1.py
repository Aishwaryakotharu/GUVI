import time,socket,sys
print("\n welcome")
print("intialising...")
time.sleep(1)
s=socket.socket()
shost=socket.gethostname()
ip=socket.gethostbyname(shost)
print(shost,"(",ip,")\n")
host=input(str("enter server address"))
name=input(str("enter your name.."))

port=5000

print("n trying to conect to",host)
time.sleep(1)
s.connect((host,port))

print("\n connectred ..\n")

s.send(name.encode())
s_name=s.recv(1024)
s_name=s_name.decode()
print(s_name,"hass connected")

while True:
    
   
    message=s.recv(1024)
    message=message.decode()
    print(s_name,":",message)
    message=input(str("me:"))
    s.send(message.encode())
