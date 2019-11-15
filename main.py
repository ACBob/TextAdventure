#another? seriously?

import socket
import player
import commandSystem
import shared

import os
import sys

import threading
import Server as ServerCode

import util

import time

from utilityprints import *


class ClientInstance:

    def __init__(self,clientData):
        self.clientData = clientData
        #We come with a socket
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self,ip,socket):
        self.clientSocket.connect((ip,socket))

    def disconnect(self):
        self.clientSocket.send('Goodbye')
        self.clientSocket.close()

    def recieveData(self):
        #dostuff
        return self.clientSocket.recv(8192) #We accept 8,192 bytes

    def sendData(self,data):
        self.clientSocket.send(data)

    def clientLoop(self):

        try:
            #while True:
            self.sendData(bytes(input('>: '),'utf-8'))
            Info(self.recieveData().decode('utf-8'))
            self.clientSocket.close()

            return
        except Exception as E:
            Debug("Error, CANCEL EVERYTHING AAAA")
            Client.clientSocket.close()

            raise E        


def mainLoop():
    #Init Stuff
    clientData = {}
    clientData['ClientName'] = socket.gethostname()
    clientData['ClientVersion'] = ['NowhereNearFinished-0',0.0]
    clientData['ClientIP'] = socket.gethostbyname(clientData['ClientName'])

    Info("Client Data: {}".format(clientData))

    Client = ClientInstance(clientData) #Create our client instance

    #Determine if we're a singleplayer session or not
    singlePlayer = True

    #Using this, get our server instance
    serverData = {}
    if singlePlayer:
        Info("Singleplayer Session.")

        serverData['ServerType'] = 'Local'
        serverData['ServerHost'] = Client.clientData['ClientName'] #We're the host, the server should know.
        
    Info("Server Data: {}".format(serverData))
    #Create our Local Server    
    Server = ServerCode.ServerInstance(serverData)

    
    Server.connect('127.0.0.1',2342)
    ServerThread = threading.Thread(target=Server.serverLoop)
    ServerThread.start()
    Client.connect('127.0.0.1',2342)
    Client.clientLoop()
    
shared.debug = True
Info("Debug. Remember to disable.")

mainLoop()
