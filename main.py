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

import random #For generating a port

from utilityprints import *
import json


class ClientInstance:

    def __init__(self,clientData):
        self.clientData = clientData
        #We come with a socket
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Connection = ()

    def __del__(self):
        self.clientSocket.close()

    def connect(self,cInfo): #cInfo -- Connection info
        self.clientSocket.connect(cInfo)

    def disconnect(self):
        self.clientSocket.send('Goodbye')
        self.clientSocket.close()

    def recieveData(self):
        #dostuff
        return self.clientSocket.recv(8192) #We accept 8,192 bytes

    def tryRecieve(self,message):

        tries = 5 #5 Attempts

        data = None

        while tries or not Data:
            tries-=1
            Info('{}, Attempt {}'.format(message,str(tries)))
            data = self.recieveData()

        if not data:
            Info('Request ran-out of attempts.')
            return None
        else:
            return data

    def sendData(self,data):
        self.clientSocket.send(bytes(data,'utf-8'))

    def sendMessage(self,messageType,messageContent,flair=None):
        self.sendData(json.dumps({'MessageType':messageType,'MessageContent':messageContent,'MessageFlair':flair}))

    def clientLoop(self):
        Debug('Beggining Client\'s Main loop')

        Debug('Attemtping Connection')
        try:
            self.connect(self.Connection)
        except (Exception,OSError) as E:
            Info('Connection Failed.')
            Debug(E)
            return -1
        Info('Connection Success')
        Debug('Requesting Server Data')
        self.sendMessage('Request','ServerData')
        
        Info(self.tryRecieve('Server Info'))
        #while not serverInfo:
        #    Debug('waiting for server data...')
        #    serverInfo = self.recieveData().decode('utf-8')
        serverInfo = json.loads(serverInfo)

        Info('Connected to {} Server @ {}'.format(serverInfo['ServerType'],serverInfo['ServerHost']))


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

    Port = random.randint(25566,36677)
    
    Server.connect('127.0.0.1',Port)
    Client.Connection = ('127.0.0.1',Port)
    ServerThread = threading.Thread(target=Server.serverLoop)
    ServerThread.start()
    Client.clientLoop()
    
shared.debug = True
Info("Debug. Remember to disable.")

mainLoop()
