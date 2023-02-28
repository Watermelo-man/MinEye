from abc import ABC, abstractmethod
import kernel
import cv2


import PIL 
#this is needed because in other case check in Picture Predict will not work
from PIL import JpegImagePlugin
from PIL import PngImagePlugin



import numpy as np
#Needs interface for raising NotImplementedError in child classes (this is check for having a realisation of  exact method in child classes)
class Imodel(ABC):

    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def showLastShot(self):
        pass

    @abstractmethod
    def returnLastResult(self):
        pass


    
    

class PictureModel(Imodel):

    last_result=None
    Kernel = None

    def __init__(self, kernel:kernel):
        self.Kernel=kernel.kernel

    def predict(self, ImageInput, size:int = 640, confCoef:float = 0.5, IoU:float = 0.5):
        if isinstance(ImageInput, PIL.JpegImagePlugin.JpegImageFile) or isinstance(ImageInput, PIL.PngImagePlugin.PngImageFile):
            self.Kernel.conf = confCoef
            self.Kernel.iou = IoU
        elif isinstance(ImageInput, np.ndarray):
            self.Kernel.conf = confCoef
            self.Kernel.iou = IoU
            ImageInput = cv2.cvtColor(ImageInput, cv2.COLOR_BGR2RGB)
        else:
            raise TypeError("Wrong type of Image, use only PIL Image Or cv2 ndarray")
        self.last_result = self.Kernel(ImageInput,size)

    def showLastShot(self):
        return self.last_result.render()[0]

    def returnLastResult(self):
        return self.last_result
        
    
class VideoModel(Imodel):

    last_result=None
    Kernel = None

    def __init__(self, kernel:kernel):
        self.Kernel=kernel.kernel

    def predict(self, ViedoInput, size:int = 640, confCoef:float = 0.5, IoU:float = 0.5):
        """"
        #make check for cv camera
        if isinstance(ViedoInput, PIL.JpegImagePlugin.JpegImageFile) or isinstance(ImageInput, PIL.PngImagePlugin.PngImageFile):
            self.Kernel.conf = confCoef
            self.Kernel.iou = IoU
        else:
            raise TypeError("Wrong type of Image, use only PIL Image Or cv2 ndarray")
        """
        shot = ViedoInput.read()
        self.last_result = self.Kernel(shot,size)

    def showLastShot(self):
        return self.last_result.render()[0]

    def returnLastResult(self):
        return self.last_result


model = kernel.kernel()

a = PictureModel(model)

cum = cv2.VideoCapture(0)

#im = cv2.cvtColor(cv2.imread("C:/Users/Alexander/Desktop/orereco/source/bottle.jpg"), cv2.COLOR_BGR2RGB)

#im = cv2.imread("C:/Users/Alexander/Desktop/orereco/source/bottle.jpg")

#cv2.imshow("input",im) 


#im = PIL.Image.open('C:/Users/Alexander/Desktop/orereco/source/bottle.jpg') 
im = 15
print(type(im))

a.predict(im)
res = a.returnLastResult()
cv2.imshow("kek",cv2.cvtColor(res.render()[0], cv2.COLOR_RGB2BGR))


cv2.waitKey(0)