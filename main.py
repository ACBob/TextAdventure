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
    s.connect(('127.0.0.1',12345))
    isRunning = True
    playerCharacter = player.spPlayer(0,0,'George')
    s.send(str(playerCharacter.getId()).encode())
    while isRunning:
        print("loop, client")
        action = input(': ')
        actionArgs = action.split(' ')[1:]
        command = action.split(' ')[0]
        if action == 'Quit':
            Info("Quit.")
            s.close()
            return 0
        else:
            #commandSystem.RunCommand(command,actionArgs,playerCharacter.getId())
            s.send(command.encode()+b';'+(','.join(actionArgs)).encode()+b';'+str(playerCharacter.getId()).encode())
            try:
                while not s.recv(1024).decode():
                    print("WAITING FOR SERVER...")
                    time.sleep(0.5)
            except BrokenPipeError:
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
time.sleep(0.1)
print("CLIENT")
ClientThread.start()
