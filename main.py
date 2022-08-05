class CameraDectorService:
    def __init__(self,inputserver,cameraRader,imageProcess,outputSocket):
        self.inputServer = inputserver
        self.cameraRader = cameraRader
        self.imageProcess = imageProcess
        self.outputSocket = outputSocket

    def Run(self):
        ipAdress = '127.0.0.1'
        port = 5005
        buffer = 1024

        print("hello world")
Q = CameraDectorService("q","v","b","g")
Q.Run()

