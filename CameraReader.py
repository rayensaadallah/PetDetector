import cv2
import usb.core
import usb.util
class CameraReader :
    def __init__(self, cameraList):
        self.cameraList = cameraList

    def initilize(self):

        dev = usb.core.find(idVendor=0x5345, idProduct=0x1234)
        if dev is None:
            raise ValueError('Device is not found')
        else :
            # device is found :-)
            if (self.cameraList == )

    def onNewImage(self):

