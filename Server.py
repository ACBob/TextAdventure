import socket
import commandSystem

def mainLoop():
   s = socket.socket()
   port = 12345
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   s.bind(('', port))
   s.listen(5)
   c, addr = s.accept()
   #print("Socket Up and running with a connection from",addr)
   while True:
         print("loop, server")
         rcvdData = c.recv(1024).decode()
         while not rcvdData:
            print("WAITING FOR CLIENT....")
         try:
            if rcvdData:
               print(rcvdData+'\n')
               splitData = rcvdData.split(';')
               print(splitData,'\n')
               command = splitData[0]
               #actionArgs = splitData[1].split(',')
               actionArgs = []
               #pId = int(splitData[2])
               pId = 1
               response = commandSystem.RunCommand(command,actionArgs,pId)
               #if type(response) == 'str': s.send(response.encode())
               #else: s.send(b'Null?!')
         except BrokenPipeError:
           pass
       #print("S:",rcvdData)
       #sendData = input("N: ")
       #c.send(sendData.encode())
       #if(sendData == "Bye" or sendData == "bye"):
       #    break
   c.close()
