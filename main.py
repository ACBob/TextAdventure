#another? seriously?

import socket
import player
import commandSystem
import shared

import os

import threading
import Server

import time

from utilityprints import *

s = socket.socket()

def mainLoop():
    Debug("Main loop")
    print('Client Main Loop')
    s.connect(('127.0.0.1',12346))
    print('Client Connected')
    isRunning = True
    playerCharacter = player.spPlayer(0,0,'George')
    s.send(('INFO'+str(playerCharacter.getId())).encode())
    print('Client Sent Needed Information.')
    while isRunning:
        print("loop, client")
        action = input(': ')
        actionArgs = action.split(' ')[1:]
        command = action.split(' ')[0]
        if action == 'Quit':
            Info("Quit.")
            s.close()
            print('Client Close Socket')
            return 0
        else:
            #commandSystem.RunCommand(command,actionArgs,playerCharacter.getId())
            s.send(b'COMMAND'+b';'+command.encode()+b';'+(','.join(actionArgs)).encode()+b';'+str(playerCharacter.getId()).encode())
            try:
                recieved = s.recv(1024).decode()
                while not recieved:
                    print("WAITING FOR SERVER...")
                    time.sleep(0.5)
                    recieved = s.recv(1024).decode()
                print('Client Recieved Response',recieved)
                if recieved == 'CRASH':
                    print('The Server Crashed somehow! Investigate.')
                    return
            except BrokenPipeError:
                print('Client Encountered Broken Pipe')
                pass



shared.debug = True
Info("Debug. Remember to disable.")

try:
    ClientThread = threading.Thread(target=mainLoop)
    ServerThread = threading.Thread(target=Server.mainLoop)
except Exception:
    pass

ServerThread.start()
print("SERVER")
time.sleep(0.5)
print("CLIENT")
ClientThread.start()
