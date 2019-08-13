import socket
import commandSystem

def mainLoop():
   print('Server Main Loop Begin')
   s = socket.socket()
   port = 12346
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   s.bind(('', port))
   print('Server Port Bound')
   s.listen(5)
   c, addr = s.accept()
   print('Server Accept Connection from',addr)
   #print("Socket Up and running with a connection from",addr)
   while True:
      print("loop, server")
      try: rcvdData = c.recv(1024).decode()
      except Exception: rcvdData = None
      while not rcvdData:
         #print("WAITING FOR CLIENT....")
         rvdData = c.recv(1024).decode()
      try:
         if rcvdData:
            print(rcvdData+'\n')
            splitData = rcvdData.split(';')
            print(splitData,'\n')
            TypeOfInfo = splitData[0]
            if TypeOfInfo == 'INFO':
               print(splitData)
            elif TypeOfInfo == 'COMMAND':
               command = splitData[1]
               actionArgs = splitData[2].split(',')
               if actionArgs == ['']:
                  actionArgs = []
               pId = int(splitData[3])
               response = commandSystem.RunCommand(command,actionArgs,pId)
               print(response)
               if response:
                    c.send(str(response).encode())
                    print('Server Sent Respone')
               else: 
                    c.send(b'Null?!')
                    print('Server Sent NULL As Response')                    
      except BrokenPipeError:
         print('Server Encountered BrokenPipe, Closing as Precaution.')
         c.send(b'CRASH')
         pass
         #c.close()
         print('Server Closed Socket')
