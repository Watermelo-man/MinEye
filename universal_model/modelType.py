from abc import ABC, abstractmethod
import kernel
import cv2
from PIL import Image
from numpy import ndarray

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
        

    def predict(self, ImagePIL:Image, size:int = 640, confCoef:float = 0.5, IoU:float = 0.5):
        self.Kernel.conf = confCoef
        self.Kernel.iou = IoU
        self.last_result = kernel(ImagePIL,size)


    def predict(self, ImageCv:ndarray, size:int = 640, confCoef:float = 0.5, IoU:float = 0.5):
        self.Kernel.conf = confCoef
        self.Kernel.iou = IoU

        #cv2.cvtColor(ImageCv.)

        #if it will be needed, BGR2RGB could be implemented
        self.last_result = self.Kernel(ImageCv,size)


    def showLastShot(self):
        return self.last_result.render()[0]

    def returnLastResult(self):
        return self.last_result
        
    

model = kernel.kernel()

a = PictureModel(model)


#im = cv2.cvtColor(cv2.imread("C:/Users/Alexander/Desktop/orereco/source/bottle.jpg"), cv2.COLOR_BGR2RGB)



#cv2.imshow("input",im) 


im = Image.open('C:/Users/Alexander/Desktop/orereco/source/bottle.jpg') 

a.predict(im)
res = a.returnLastResult()
cv2.imshow("kek",res.render()[0])


cv2.waitKey(0)