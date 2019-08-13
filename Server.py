import socket
import commandSystem
import player

import util

global ConnectedClients
ConnectedClients = []

def mainLoop():
   print('Server Main Loop Begin')
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   port = 12346
   s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   s.bind(('', port))
   print('Server Port Bound')
   #s.listen(5)
   #c, addr = s.accept()
   #print('Server Accept Connection from',addr)
   #print("Socket Up and running with a connection from",addr)
   while True:
      print("loop, server")
      try: rcvdData = s.recvfrom(1024)
      except Exception: rcvdData = None
      while not rcvdData:
         #print("WAITING FOR CLIENT....")
         rcvdData = s.recvfrom(1024)
      try:
         if rcvdData:
            Address = rcvdData[1]
            print(rcvdData,'\n')
            splitData = rcvdData[0].decode().split(';')
            print(splitData,'\n')
            TypeOfInfo = splitData[0]
            if TypeOfInfo == 'INFO':
               print(splitData)
               if splitData[1] == 'I WANT PLAYER':
                  print(Address,'Wants a player.')
                  s.sendto(str(player.spPlayer(0,0,splitData[2]).getId()).encode(),Address)
                  ConnectedClients.append(Address)
               elif splitData[1] == 'I HAVE QUIT':
                  ID = splitData[2]
                  print(Address,'Has Quit.')
                  util.RemovePlayer(ID)
                  ConnectedClients.remove(Address)
                  
            elif TypeOfInfo == 'COMMAND':
               command = splitData[1]
               actionArgs = splitData[2].split(',')
               if actionArgs == ['']:
                  actionArgs = []
               pId = int(splitData[3])
               response = commandSystem.RunCommand(command,actionArgs,pId)
               print(response)
               if response:
                    if not command == 'Say': s.sendto(str(response).encode(),Address)
                    else:
                        for Client in ConnectedClients:
                           s.sendto(str(response).encode(),Client)
                    print('Server Sent Respone')
               else: 
                    s.send(b'Null?!')
                    print('Server Sent NULL As Response')                    
      except BrokenPipeError:
         print('Server Encountered BrokenPipe, Closing as Precaution.')
         s.send(b'CRASH')
         pass
         #c.close()
         print('Server Closed Socket')

if __name__ == "__main__":
   mainLoop()
