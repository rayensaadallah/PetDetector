import os
import socket
import sys


class OutputSocket:

    ListClient = []
    data = open('_data.txt','a+')
    data.seek(0)
    def __init__(self, PetName,ConfidanceZone,OutputX,OutputY):
        self.PetName =PetName
        self.ConfidanceZone =ConfidanceZone
        self.Output = OutputX
        self.OutputY = OutputY

    def initilize(self, client, name, ip, port, buffer):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            print("port connected")
            OutputSocket.ListClient.append(name)
            if os.stat(OutputSocket.data).st_size == 0:
                print('No new information')
            else:
                client.send(OutputSocket.data.readline(),"utf-8")
                OutputSocket.data.truncate()#but if ther is more than 1 client who didnt resive the msg only the first one will get notified
        except:
            client.send(bytes("this port already used", "utf-8"))
            sys.exit(-1)

    def sendDetectedPet(self, client, text):
        try:
            for i in OutputSocket.ListClient:
                client.send(text,"utf-8")
            print("All client got the data ")
        except:
            print("there is no client connected ")
            OutputSocket.data.write(text)
        #neb34ou les donner lel client bel set configuration



 #nestna3 tcp socket w w n5alih lisning w ken el port reserve tsir error
#n7el tcp socket nestana 3ala infiini si client connected sauvgardi n7otou
# 3andi w i4a imag eprocc tel9a pet t3ayet send detected pet tchouf des client
# connecte 3aliya ena ken fama client connect teb3a4lou info
#retained msg first thing
#nejmou nsaviw el donner wa9 client is connected yeb34ou
