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
    confidence = 0.5
    last_result=None
    Kernel = None
    compute_type = None
    contrast = 0
    brightness = 0
    def __init__(self, ker:kernel.kernel):
        self.Kernel=ker.kernel
        self.compute_type = ker.mode_type


    def resize_image(self,image, target_width=1024):
        # Загрузка изображения
        
        
        # Получение исходных размеров изображения
        height, width, _ = image.shape

        # Вычисление новой высоты с сохранением соотношения сторон
        new_height = int(height * (target_width / width))

        # Изменение размера изображения
        resized_image = cv2.resize(image, (target_width, new_height))
        return resized_image

    def apply_contrast(self,input_img, contrast = 1):
       # CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=contrast, tileGridSize=(8,8))

        lab = cv2.cvtColor(input_img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
        l, a, b = cv2.split(lab)  # split on 3 different channels

        l2 = clahe.apply(l)  # apply CLAHE to the L-channel

        lab = cv2.merge((l2,a,b))  # merge channels
        img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
        return img2


    def apply_brightness(self,shot,brightness):
        shot = cv2.addWeighted(shot , 1,np.zeros(shot.shape,shot.dtype),0,brightness)
        return shot
        
    def predict(self, ImageInput, confCoef:float = 0.5,contrast:float = 0,brightness:float=0):# IoU:float = 0.5):
        #print("pic")
        # if isinstance(ImageInput, PIL.JpegImagePlugin.JpegImageFile) or isinstance(ImageInput, PIL.PngImagePlugin.PngImageFile):
        #     pass
        # else:
        #     raise TypeError("Wrong type of Image, use only PIL Image Or cv2 ndarray")
        ImageInput = self.resize_image(ImageInput)

        self.contrast = contrast
        self.confidence = confCoef
        self.brightness = brightness
    
        if self.brightness!=0:
      
            ImageInput = self.apply_brightness(ImageInput,brightness)

        if self.contrast >0:
            ImageInput = self.apply_contrast(ImageInput,self.contrast)

        #ImageInput = cv2.cvtColor(ImageInput, cv2.COLOR_BGR2RGB)

        if self.compute_type == 'cpu':
            self.last_result = self.Kernel(ImageInput,verbose = False,device="cpu",conf = self.confidence)#,size)
        if self.compute_type == 'cuda':
            self.last_result = self.Kernel(ImageInput,verbose = False,device=0,conf = self.confidence)

    def showLastShot(self):
        if self.last_result != None:
            return cv2.cvtColor(self.last_result[0].plot(), cv2.COLOR_BGR2RGB)
        else:
            return None
        #return self.last_result[0].plot()#.boxes#render()[0]
    def showLastResult(self):
        if self.last_result != None:
            return self.last_result[0].boxes.data
        else:
            #print('False')
            return None
        #return cv2.cvtColor(self.last_result.render()[0], cv2.COLOR_BGR2RGB)
        #return self.last_result
    def showLastSizes(self):
        if self.last_result != None:
            if self.last_result[0].masks != None:
                return self.last_result[0].masks.data
            else:
                #print('False')
                return None
        else:
            #print('False')
            return None
        
class VideoModel(Imodel):
    confidence = 0.5
    contrast = 0
    brightness = 0
    last_result=None
    Kernel = None
    compute_type = None
    def __init__(self, ker:kernel.kernel):
        self.Kernel=ker.kernel
        self.compute_type = ker.mode_type


    def resize_image(self,image, target_width=1024):
        # Загрузка изображения
        
        
        # Получение исходных размеров изображения
        height, width, _ = image.shape

        # Вычисление новой высоты с сохранением соотношения сторон
        new_height = int(height * (target_width / width))

        # Изменение размера изображения
        resized_image = cv2.resize(image, (target_width, new_height))
        return resized_image


    def apply_contrast(self,input_img, contrast = 1):
       # CLAHE (Contrast Limited Adaptive Histogram Equalization)
        clahe = cv2.createCLAHE(clipLimit=contrast, tileGridSize=(8,8))
        
        lab = cv2.cvtColor(input_img, cv2.COLOR_BGR2LAB)  # convert from BGR to LAB color space
        l, a, b = cv2.split(lab)  # split on 3 different channels

        l2 = clahe.apply(l)  # apply CLAHE to the L-channel

        lab = cv2.merge((l2,a,b))  # merge channels
        img2 = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)  # convert from LAB to BGR
        return img2
       
    def apply_brightness(self,shot,brightness):
            shot = cv2.addWeighted(shot , 1,np.zeros(shot.shape,shot.dtype),0,brightness)
            return shot

    def predict(self, ImageInput:cv2.VideoCapture, confCoef:float = 0.5,contrast:float = 0,brightness=0 ):#, IoU:float = 0.5):
        """"
        #make check for cv camera
        if isinstance(ViedoInput, PIL.JpegImagePlugin.JpegImageFile) or isinstance(ImageInput, PIL.PngImagePlugin.PngImageFile):
            self.Kernel.conf = confCoef
            self.Kernel.iou = IoU
        else:
            raise TypeError("Wrong type of Image, use only PIL Image Or cv2 ndarray")
        """
        self.contrast = contrast
        self.confidence = confCoef
        self.brightness = brightness
        #self.Kernel.conf = confCoef
        #self.Kernel.iou = IoU
        
        ret, shot = ImageInput.read()

        shot = self.resize_image(shot)

        if self.brightness != 0:
            shot = self.apply_brightness(shot,self.brightness)

        if self.contrast >0:
            shot = self.apply_contrast(shot,self.contrast)
            #print(self.contrast)
            #shot = cv2.addWeighted(shot , 1,np.zeros(shot.shape,shot.dtype),0,self.contrast)

        

        if self.compute_type == 'cpu':
            self.last_result = self.Kernel(shot,verbose = False,device = "cpu",conf = self.confidence)
        if self.compute_type == 'cuda':
            self.last_result = self.Kernel(shot,verbose = False,device = 0,conf = self.confidence)

    def showLastShot(self):
        if self.last_result != None:
        #print(self.last_result)
            return cv2.cvtColor(self.last_result[0].plot(), cv2.COLOR_BGR2RGB)
        #return self.last_result[0].plot()
        else:
            #print('False')
            return None
    def showLastResult(self):
        if self.last_result != None:
            if self.last_result[0].masks != None:
                return self.last_result[0].boxes.data
            
        
        #return self.last_result[0].plot()
    def showLastSizes(self):
        if self.last_result != None:
            if self.last_result[0].masks != None:    
                return self.last_result[0].masks.data
            else:
                    print('False')
                    return None
        else:
            print('False')
            return None

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
