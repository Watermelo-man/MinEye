from abc import ABC, abstractmethod
import kernel
import PIL

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

    last_reslt=None
    Kernel = None

    def __init__(self, kernel:kernel):
        self.Kernel=kernel.kernel
        
    

    def predict(self, Image:PIL.Image, ):
        pass

    def showLastShot(self):
        pass

    #def returnLastResult(self):
     #   pass
        
    
a = PictureModel()
        
    