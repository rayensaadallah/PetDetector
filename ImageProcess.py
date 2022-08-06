import cv2, time, os, tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.python.keras.utils.data_utils import get_file
np.random.seed(20)

class ImageProcess :
    def __init__(self, configuration):

        self.configuration = configuration

    def onNewImage(self):

        camera = cv2.VideoCapture(0)  # 0 for webcam and 1 for USB camera or path file of the video
        count = 0
        while True:
            ret, frame = camera.read()
            if ret == True:
                cv2.imshow("test", frame)
                # cv2.imwrite("capture_video/frame"+str(count)+".jpg", frame)
                cv2.imwrite("{}.jpg".format(count), frame)
                count += 1
                key = cv2.waitKey(1)  # 1 milliseconde
                if key == ord("q"):
                    break
            else:
                print("error reading by yessin")
        camera.release()
        cv2.destroyAllWindows()

    def setConfiguration(self):

        modelURL = "http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz"
        classFile = "coco.names"
        imagePath = "index.jpeg"
        threshold = 0.5

        ImageProcess.readClasses(classFile)
        ImageProcess.downloadModel(modelURL)
        ImageProcess.loadModel()
        ImageProcess.predictImage(imagePath)
        ImageProcess.result()

    def result(self, data):

        return [petname, ]

    def collisionDetection(self, data ):

        nameIS = data[0]
        xIS = data[1]
        yIS = data[2]
        widthIS = data[3]
        heightIS = data[4]
        if ( xmin > xIS + widthIS && xIS > xmin + width && ymax > yIS + heightIS && yIS > ymax + height) :
            r = 1
        else :
            r = 0

        return [r, petname, xmin, ymax, confidencezone]



    def readClasses(self, classesFilePath):

        with open(classesFilePath, 'r') as f:
            self.classesList = f.read().splitlines()
            # colors list
            self.colorList = np.random.uniform(low=0, high=255, size=(len(self.classesList), 3))
            print(len(self.classesList), len(self.colorList))

    def downloadModel(self, modelURL):

        fileName = os.path.basename(modelURL)
        self.modelName = fileName[:fileName.index('.')]
        print(self.modelName)
        self.cacheDir = "./pretraind_models"
        os.makedirs(self.cacheDir, exist_ok=True)
        get_file(fname=fileName, origin=modelURL, cache_dir=self.cacheDir, cache_subdir="checkpoint", extract=True)

    def loadModel(self):

        print("Loading Model" + self.modelName)
        tf.keras.backend.clear_session()
        self.model = tf.saved_model.load(
        os.path.join(self.cacheDir, "checkpoint", self.modelName, "saved_model"))
        print("Model" + self.modelName + "loaded successfully ...")

    def createBoundigBox(self, image, threshold=0.5):

        inputTensor = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
        # inputTensor= cv2.cvtColor(image.copy(), cv2.COLOR_BGR2RGB)
        inputTensor = tf.convert_to_tensor(inputTensor, dtype=tf.uint8)
        inputTensor = inputTensor[tf.newaxis, ...]
        detections = self.model(inputTensor)
        bboxs = detections['detection_boxes'][0].numpy()
        classIndexes = detections['detection_classes'][0].numpy().astype(np.int32)
        classScores = detections['detection_scores'][0].numpy()

        imH, imW, imC = image.shape

        bboxIdx = tf.image.non_max_suppression(bboxs, classScores, max_output_size=15, iou_threshold=threshold, score_threshold=threshold)
        print("creating boundig box ")

        if len(bboxIdx) != 0:
            for i in bboxIdx:
                bbox = tuple(bboxs[i].tolist())
                classConfidence = round(100 * classScores[i])
                classIndexe = classIndexes[i]
                classLabelText = self.classesList[classIndexe].upper()
                classColor = self.colorList[classIndexe]
                displayText = '{}: {}%'.format(classLabelText, classConfidence)
                ymin, xmin, ymax, xmax = bbox
                xmin, xmax, ymin, ymax = (xmin * imW, xmax * imW, ymin * imH, ymax * imH)
                xmin, xmax, ymin, ymax = int(xmin), int(xmax), int(ymin), int(ymax)

                #method result
                width = xmax - xmin
                height = ymax - ymin


                #method result

                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), color=classColor, thickness=1)
                cv2.putText(image, displayText, (xmin, ymin - 10), cv2.FONT_HERSHEY_PLAIN, 1, classColor, 2)
                # el ajneb mta3 el cadre (box) #
                lineWidth = min(int((xmax - xmin) * 0.2), int((ymax - ymin) * 0.2))
                cv2.line(image, (xmin, ymin), (xmin + lineWidth, ymin), classColor, thickness=5)
                cv2.line(image, (xmin, ymin), (xmin, ymin + lineWidth), classColor, thickness=5)
                cv2.line(image, (xmax, ymin), (xmax - lineWidth, ymin), classColor, thickness=5)
                cv2.line(image, (xmax, ymin), (xmax, ymin + lineWidth), classColor, thickness=5)
                cv2.line(image, (xmin, ymax), (xmin + lineWidth, ymax), classColor, thickness=5)
                cv2.line(image, (xmin, ymax), (xmin, ymax - lineWidth), classColor, thickness=5)
                cv2.line(image, (xmax, ymax), (xmax - lineWidth, ymax), classColor, thickness=5)
                cv2.line(image, (xmax, ymax), (xmax, ymax - lineWidth), classColor, thickness=5)
                ##print les donner eli 7achetna bihom
                print(self.classesList[classIndexe], classConfidence, xmin, xmax, ymin, ymax)
        return image

    def predictImage(self, imagePath):

        image = cv2.imread(imagePath)
        bboxImage = self.createBoundigBox(image)
        cv2.imwrite(self.modelName + ".jpg", bboxImage)
        #cv2.imshow("Result", bboxImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return bboxImage



