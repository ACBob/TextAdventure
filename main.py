#another? seriously?

import socket
import player
import commandSystem
import shared

import os
import sys

import threading
import Server

import util

import time

from utilityprints import *

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def WaitForResponse():
    try:
        recieved = s.recvfrom(1024)[0].decode()
        while not recieved:
            print("WAITING FOR SERVER...")
            time.sleep(0.5)
            recieved = s.recvfrom(1024)[0].decode()
        print('Client Recieved Response',recieved)
        return recieved
        if recieved == 'CRASH':
            print('The Server Crashed somehow! Investigate.')
            return
    except BrokenPipeError:
        print('Client Encountered Broken Pipe')
        pass

def mainLoop():
    Debug("Main loop")
    print('Client Main Loop')
    global IP
    global Port
    global Name
    if Flags[0] == 'Multi':
        IP = ''
        Port = ''
        Name = ''
        while IP == '':
            IP = input('IP? ')
        while Port == '':
            Port = int(input('PORT? '))
        while Name == '':
            Name = input('NAME? ')
        try: s.connect((IP,int(Port)))
        except ConnectionRefusedError:
            print('Connection Refused!')
            return
        except Exception as e:
            print(e)
            return
    else:
        IP = '127.0.0.1'
        Port = 12346
        Name = 'Simon'
        s.connect((IP,Port))
    print('Client Connected')
    isRunning = True
    #playerCharacter = player.spPlayer(0,0,'George')
    s.sendto(('INFO'+';'+'I WANT PLAYER'+';'+Name).encode(),(IP,Port))#+str(playerCharacter.getId())).encode(),(IP,Port))
    print('Client Sent Needed Information.')
    #playerCharacter = util.getPlayerFromId(int(WaitForResponse()))
    OurId = int(WaitForResponse())
    while isRunning:
        print("loop, client")
        readLetter = sys.stdin.read(1)
        MagicCommandFixer.append(readLetter)
        action = MagicCommandFixer.split('\n')[0]
        actionArgs = action.split(' ')[1:]
        command = action.split(' ')[0]
        if action == 'Quit':
            Info("Quit.")
            s.sendto(('INFO'+';'+'I HAVE QUIT'+';'+str(OurId)).encode(),(IP,Port))
            s.close()
            print('Client Close Socket')
            return 0
        else:
            #commandSystem.RunCommand(command,actionArgs,playerCharacter.getId())
            s.send(b'COMMAND'+b';'+command.encode()+b';'+(','.join(actionArgs)).encode()+b';'+str(OurId).encode())#+str(playerCharacter.getId()).encode())
            WaitForResponse()



shared.debug = True
Info("Debug. Remember to disable.")

try:
    ClientThread = threading.Thread(target=mainLoop)
    ServerThread = threading.Thread(target=Server.mainLoop)
except Exception:
    pass

#Flags = sys.argv
#print(Flags)

Flags = ['Multi']


if not Flags[0] == 'Multi': ServerThread.start()
#print("SERVER")
time.sleep(0.5)
print("CLIENT")
ClientThread.start()
