import time,socket,sys,errno
print("\n welcome")
print("intialising...")
time.sleep(1)
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
ip=socket.gethostbyname(host)
port=5000
s.bind((host,port))
print(host,"(",ip,")\n")
name=input(str("enter your name.."))
s.listen(1)
print("\n waititng")
conn,addr=s.accept()
print("received from",addr[0],"(",addr[1])
s_name=conn.recv(1024)
s_name=s_name.decode()
print(s_name,"hass connected")
conn.send(name.encode())
while True:
    message=input(str("me:"))
    conn.send(message.encode())
    message=conn.recv(1024)
    message=message.decode()
    print(s_name,":",message)
