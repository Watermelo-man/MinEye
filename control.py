import sys
from pathlib import Path
import universal_model 
import cv2
from PIL import Image
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QFileDialog
from enum import Enum
import os
from collections import Counter
import torch
class types(Enum):
    photo = 1
    video = 2


class controller():
    model = None
    source = None
    source_width = None
    source_height = None
    kernel = None


    __computeDevice = "kek"

    __currentType = types.photo

    __modelpth = str(os.path.dirname(os.path.abspath(__file__)))

    __modelpth = os.path.join(__modelpth,'ourmodels')

    __modelpth = os.path.join(__modelpth,'yolov8n.pt')

    #__modelpth = r"C:\Projects\orereco\ourmodels\yolov5x.pt"

    def __init__(self):
         self.kernel = universal_model.kernel.kernel(model_path=self.__modelpth)#, device=self.__computeDevice)


    #def chooseComputeDevice():
       # try:


         
    def changeModelPath(self,pth:str)->None:
        self.__modelpth = pth
        self.kernel = universal_model.kernel.kernel(model_path=self.__modelpth)#,device=self.__computeDevice)
        self.selectType(self.__currentType)


    def selectType(self,type:int):
        if type == 1:
            self.model = universal_model.modelType.models.selectModel(self.kernel.kernel, "PictureModel")

            return 0
        elif type == 2:
            self.model = universal_model.modelType.models.selectModel(self.kernel.kernel, "VideoModel")
            return 0
        else:
            return -1
        
    
    def selectSource(self,src:int = 1):
        if src == 1:
            self.path, self.check = QFileDialog.getOpenFileName(None, "Open File", "", "Image Files (*.png *.jpg);; Video Files (*.mp4 *.flv *.ts *.mts *.avi)")
            if Path(str(self.path)).suffix in ['.mp4', '.flv', '.ts', '.mts', '.avi']:
                self.selectType(2)
                #print("video")
                self.source = cv2.VideoCapture(str(self.path))
                self.__currentType = 2
            else:
                self.selectType(1)
                self.source = Image.open(str(self.path))
                self.__currentType = 1
            return 0
        elif src == 2:
            self.selectType(2)
            #print("camera")
            self.source = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            self.__currentType = 2
            return 0
        else:
            return -1
        
    point1 = (100,100)
    point2 = (200,200)    
    
    def analyseShot(self):#(model:universal_model.modelType.Imodel = md,im = im):
        
        #height, width, channels = self.source.shape
        #print(height,width)
        self.model.predict(self.source)
        self.res = self.model.showLastShot()
        #cv2.imshow("lol",self.res)
        #cv2.waitKey(0)
        #print(type(self.model))
        #if type(self.model)==universal_model.modelType.VideoModel:
        #    self.res = cv2.cvtColor(self.res, cv2.COLOR_BGR2RGB)
        # if self.point1:
        #     cv2.circle(self.res, self.point1, 5, (0, 255, 0), -1)
        if self.point1 and self.point2:
            cv2.circle(self.res, self.point1, 15, (0, 255, 0), -1)
            cv2.circle(self.res, self.point2, 15, (0, 255, 0), -1)
            cv2.line(self.res, self.point1, self.point2, (255, 0, 0), 10)
        #cv2.circle(self.res, (10,10), 5, (0, 255, 0), -1)
        #cv2.imshow('kek',self.res)

        #create from numpy Qpixmap
        h,w,ch = self.res.shape
        bytes_per_line = ch*w
        convert_to_Qt_format = QImage(self.res.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        #create from numpy Qpixmap
        #print("shot exist")
        #cv2.waitKey(0)
        return convert_to_Qt_format
    

    def CountShot(self):
            classes:dict = self.kernel.kernel.names
            #new_dict = dict()
            allkeys = classes.keys()
            #print(allkeys)
            print(classes)
            if self.model != None:
                boxes = self.model.showLastResult()
            else:
                print('kek')
                return classes_count
            clss = boxes[:, 5]
            #print(classes)
            #print(boxes)
            
            #print(classes) 
            count = Counter(clss.long().tolist())
            resultcounter = {str(k): v for k, v in count.items()}
            classes_count = {classes[int(k)]: v for k, v in resultcounter.items()}


            #classes_size = {classes[int(k)]: v for k, v in resultcounter.items()}

            print(classes_count)
            return classes_count
    

    def CountSquare(self,classes_in_shot:dict):
        classes:dict = self.kernel.kernel.names
        #print(classes)
        inv_classes = dict((v, k) for k, v in classes.items())
        result = dict()
        boxes = self.model.showLastResult()
        masks = self.model.showLastSizes()
        clss = boxes[:, 5]
        exist_keys = list(classes_in_shot.keys())
        for key in exist_keys:
            item_indicies = torch.where(clss == inv_classes[key])
            item_masks = masks[item_indicies]
            item_mask = torch.any(item_masks,dim = 0).int() * 255
            image_mask = item_mask.cpu().numpy().astype('uint8')
            cntw = cv2.countNonZero(image_mask)
            result[key] = cntw
        return result

cont = controller()
