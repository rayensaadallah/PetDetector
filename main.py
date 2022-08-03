class CameraDectorService:
    def __init__(self,inputserver,cameraRader,imageProcess,outputSocket):
        self.inputServer = inputserver
        self.cameraRader = cameraRader
        self.imageProcess = imageProcess
        self.outputSocket = outputSocket

    def Run(self):
        print("hello world")
Q = CameraDectorService("q","v","b","g")
Q.Run()

