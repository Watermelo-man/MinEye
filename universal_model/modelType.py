from abc import ABC, abstractmethod 
from . import kernel
#import kernel
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
    def showLastResult(self):
        pass
    
    @abstractmethod
    def showLastSizes(self):
        pass

class PictureModel(Imodel):

    last_result=None
    Kernel = None

    def __init__(self, ker:kernel.kernel.kernel):

        self.Kernel=  ker

    def predict(self, ImageInput, size:int = 640, confCoef:float = 0.5, IoU:float = 0.5):
        #print("pic")
        if isinstance(ImageInput, PIL.JpegImagePlugin.JpegImageFile) or isinstance(ImageInput, PIL.PngImagePlugin.PngImageFile):
            pass
        else:
            raise TypeError("Wrong type of Image, use only PIL Image Or cv2 ndarray")
        self.last_result = self.Kernel(ImageInput)#,size)

    def showLastShot(self):
        return cv2.cvtColor(self.last_result[0].plot(), cv2.COLOR_BGR2RGB)
        #return self.last_result[0].plot()#.boxes#render()[0]
    def showLastResult(self):
        return self.last_result[0].boxes.data
     
        #return cv2.cvtColor(self.last_result.render()[0], cv2.COLOR_BGR2RGB)
        #return self.last_result
    def showLastSizes(self):
        return self.last_result[0].masks.data
        
    
class VideoModel(Imodel):

    last_result=None
    Kernel = None

    def __init__(self, ker:kernel.kernel.kernel):
        self.Kernel=ker

    def predict(self, VideoInput:cv2.VideoCapture, size:int = 640, confCoef:float = 0.5, IoU:float = 0.5):
        """"
        #make check for cv camera
        if isinstance(ViedoInput, PIL.JpegImagePlugin.JpegImageFile) or isinstance(ImageInput, PIL.PngImagePlugin.PngImageFile):
            self.Kernel.conf = confCoef
            self.Kernel.iou = IoU
        else:
            raise TypeError("Wrong type of Image, use only PIL Image Or cv2 ndarray")
        """

        #self.Kernel.conf = confCoef
        #self.Kernel.iou = IoU
        
        ret, shot = VideoInput.read()

        self.last_result = self.Kernel(shot)


    def showLastShot(self):
        #print(self.last_result)
        return cv2.cvtColor(self.last_result[0].plot(), cv2.COLOR_BGR2RGB)
        #return self.last_result[0].plot()

    def showLastResult(self):
        return self.last_result[0].boxes.data
        #return self.last_result[0].plot()
    def showLastSizes(self):
        return self.last_result[0].masks.data


class fabric():
    inputType = dict()

    def __init__(self):
        pass

    def addType(self, typeStr:str, typeClass):
         self.inputType.update({typeStr:typeClass})
         print(self.inputType)

    def selectModel(self, Kernel:kernel.kernel.kernel, type:str = "PictureModel"):
        if self.inputType.get(type) is not None:    
            return self.inputType[type](Kernel)  
        else: 
            #print("Ty petooh")
            return -1

models = fabric()
models.addType("PictureModel",PictureModel)
models.addType("VideoModel",VideoModel)
