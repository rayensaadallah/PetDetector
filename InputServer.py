import json
import socket
class InputServer:
    serverTcpSocket = "127.0.0.1"
    port = 1024
    listConnectedSocker = []
    def __int__(self, name, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def initializ(self):
        port += 1
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if (server.connect_ex((serverTcpSocket, port)) == 0):
            InputServer.onError()
        else:
            server.bind((serverTcpSocket, port))
            server.listen(5)
            client, address = server.accept()

    def onNewSocket(self):
        listConnectedSocker.append(self.name)


    def onMessageRecived(self):

        objectRecived = client.recv(1024) # cheniya hal 1024 : hiya buffer -> speed haja ki haka ?

        return objectRecived

    def onError(self):
        pass

    def processMessage(self, objectRecived):

        dictObject = json.loads(objectRecived) #  {"name": ismail, "x": 50, "y": 60, "width": 200, "height": 100}
        name = dictObject["name"]
        x = dictObject["x"]
        y = dictObject["y"]
        width = dictObject["width"]
        height = dictObject["height"]

        return [name, x, y, width, height]


