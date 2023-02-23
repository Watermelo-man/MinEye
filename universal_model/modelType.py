
import cv2
import PIL
from kernel import *
import yolov5


class modelIMGPIL():
    Kernel:yolov5
    last_result = None

    def __init__(self, Kernel:kernel):
        self.Kernel = Kernel
        
    def predict(self,image:PIL.Image , image_size:int, confcoeff:float, iou:float):
        if confcoeff!=None or iou!=None:
            self.Kernel.conf = confcoeff
            self.Kernel.iou = iou
        else:
            self.Kernel.conf = 0
            self.Kernel.iou = 0
        self.last_result =  self.Kernel([image], size=image_size)

    def _show_last_result(self):
        if self.last_result!= None:
            return self.last_result.render()[0]
        else:
            return None

class modelVideoCapture(): ## NEEDS TO CHANGE, IT DOESNT WORK
    Kernel:yolov5
    last_result = None
    camera = None
    def __init__(self, Kernel:kernel):
        self.Kernel = Kernel
        


    def predict(self,camera , image_size:int, confcoeff:float, iou:float):


        ret, shot = camera.read()
    



       # shot = cv2.cvtColor(shot, cv2.COLOR_BGR2RGB)
        shot_pil = PIL.Image.fromarray(shot)




        if confcoeff!=None or iou!=None:
            self.Kernel.conf = confcoeff
            self.Kernel.iou = iou
        else:
            self.Kernel.conf = 0
            self.Kernel.iou = 0
        self.last_result =  self.Kernel([shot_pil], size=image_size)

    def _show_last_result(self):
        if self.last_result!= None:
            
            return self.last_result.render()[0]
        else:
            
            return None
        


#make pseudo-fabric

class fabric():

    inputType = dict()
   
    def __init__(self):
        pass

    def addType(self, typeStr:str, typeClass):
         self.inputType.update({typeStr:typeClass})

    def selectModel(self, Kernel:kernel, type:str = "IMGPIL"):
        if self.inputType.get(type) is not None:    
            return self.inputType[type](Kernel.kernel)  
        else: 
            print("Ty petooh")
            return -1