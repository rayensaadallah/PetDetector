import socket

class OutputSocket:

    def __init__(self, PetName,ConfidanceZone,OutputX,OutputY):
        self.PetName =PetName
        self.ConfidanceZone =ConfidanceZone
        self.Output = OutputX
        self.OutputY = OutputY

    def initilize(self,ip,port,buffer):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if (s.connect_ex((ip, port)) == 0):
            s.connect((ip,port))
            print("port connected")

        else:
            OutputSocket.onError(1)


    def onError(self,errorNbr):
        if errorNbr  ==1:
            print("port not available")
            OutputSocket.port=OutputSocket.port+1
        if errorNbr == 2:
            print("error slata mechwiya ")
        else:
            print("aze")


    def sendDetectedPet(self):
        print("detected")

 #nestna3 tcp socket w w n5alih lisning w ken el port reserve tsir error
#n7el tcp socket nestana 3ala infiini si client connected sauvgardi n7otou 3andi w i4a imag eprocc tel9a pet t3ayet send detected pet tchouf des client connecte 3aliya ena ken fama client connect teb3a4lou info si mech connected teb3a4 el on error w hiya t9oul el cliet rahou discnnected
