class OutputSocket:
    def __init__(self,PetName,ConfidanceZone,OutputX,OutputY):
        self.PetName =PetName
        self.ConfidanceZone =ConfidanceZone
        self.Output = OutputX
        self.OutputY = OutputY

    def initilize(self):
        print("first")

    def onError(self):
        print("error")

    def sendDetectedPet(self):
        print("detected")
