import sys
from pathlib import Path
import universal_model 
import cv2
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import QtCore
from PyQt6.QtWidgets import QFileDialog
from enum import Enum
import os
from collections import Counter
import torch
import PIL
import numpy

class types(Enum):
    photo = 1
    video = 2


class controller():
    model = None
    source = None
    source_width = None
    source_height = None
    kernel = None
    scale_value = 1 #in mm
    onepixdim = 0
    __computeDevice = "kek"

    __currentType = types.photo

    __modelpth = str(os.path.dirname(os.path.abspath(__file__)))

    __modelpth = os.path.join(__modelpth,'ourmodels')

    __modelpth = os.path.join(__modelpth,'yolov8n.pt')

    #__modelpth = r"C:\Projects\orereco\ourmodels\yolov5x.pt"

    def __init__(self):
         self.kernel = universal_model.kernel.kernelinst#, device=self.__computeDevice)


    #def chooseComputeDevice():
       # try:


         
    def changeModelPath(self,pth:str)->None:
        self.__modelpth = pth
         #self.kernel = universal_model.kernel.kernelinst.change_model(self.__modelpth)
        self.kernel.change_model(self.__modelpth)
        #,device=self.__computeDevice)
        self.selectType(self.__currentType)


    def selectType(self,type:int):
        if type == 1:
            self.model = universal_model.modelType.models.selectModel(self.kernel, "PictureModel")

            return 0
        elif type == 2:
            self.model = universal_model.modelType.models.selectModel(self.kernel, "VideoModel")
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
                self.source = cv2.imread(str(self.path)) #Image.open(str(self.path))
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
        
    point1 = None
    point2 = None    
    point3 = None
        
    def analyseShot(self):#(model:universal_model.modelType.Imodel = md,im = im):
        
        #height, width, channels = self.source.shape
        #print(height,width)
       
        if isinstance(self.source, cv2.VideoCapture):
            ret, shot = self.source.read()
        else:
            shot = self.source

        try:
            height, width, channels = shot.shape
        except:
            print('No image/video found')
            black = QImage()
            black.fill(QtCore.Qt.GlobalColor.black)
            return black
        #print(height, width)
        self.model.predict(self.source)
        self.res = self.model.showLastShot()
        # DRY KISS EXAMPLE
        if self.point1:
            cv2.circle(self.res, (int(self.point1[0] * float(width/800)),int(self.point1[1] * float(height/600))), 15, (0, 255, 0), -1)
        if self.point1 and self.point2:
            cv2.circle(self.res, (int(self.point1[0] * float(width/800)),int(self.point1[1] * float(height/600))), 15, (0, 255, 0), -1)
            cv2.circle(self.res, (int(self.point2[0] * float(width/800)),int(self.point2[1] * float(height/600))), 15, (0, 255, 0), -1)
            cv2.line(self.res, (int(self.point1[0] * float(width/800)),int(self.point1[1] * float(height/600))), (int(self.point2[0] * float(width/800)),int(self.point2[1] * float(height/600))), (255, 0, 0), 10)
        if self.point1 and self.point2 and self.point3:
            cv2.circle(self.res, (int(self.point1[0] * float(width/800)),int(self.point1[1] * float(height/600))), 15, (0, 255, 0), -1)
            cv2.circle(self.res, (int(self.point2[0] * float(width/800)),int(self.point2[1] * float(height/600))), 15, (0, 255, 0), -1)
            cv2.line(self.res, (int(self.point1[0] * float(width/800)),int(self.point1[1] * float(height/600))), (int(self.point2[0] * float(width/800)),int(self.point2[1] * float(height/600))), (255, 0, 0), 10)

            cv2.circle(self.res, (int(self.point3[0] * float(width/800)),int(self.point3[1] * float(height/600))), 15, (0, 255, 0), -1)
            
            cv2.line(self.res, (int(self.point2[0] * float(width/800)),int(self.point2[1] * float(height/600))), (int(self.point3[0] * float(width/800)),int(self.point3[1] * float(height/600))), (0, 0, 255), 10)


            self.xpixlength = ((int(self.point2[0] * float(width/800)) - int(self.point1[0] * float(width/800)))**2 + (int(self.point2[1] * float(height/600)) - int(self.point1[1] * float(height/600)))**2 )**0.5
            self.ypixlength = ((int(self.point3[0] * float(width/800)) - int(self.point2[0] * float(width/800)))**2 + (int(self.point3[1] * float(height/600)) - int(self.point2[1] * float(height/600)))**2 )**0.5
            
            self.onepixdim = self.scale_value/self.xpixlength * self.scale_value/self.ypixlength
        
        h,w,ch = self.res.shape
        bytes_per_line = ch*w
        convert_to_Qt_format = QImage(self.res.data, w, h, bytes_per_line, QImage.Format.Format_RGB888).scaled(800,600)#,QtCore.Qt.AspectRatioMode.KeepAspectRatio)

        return convert_to_Qt_format
    

    def CountShot(self):
            classes:dict = self.kernel.kernel.names
            #allkeys = classes.keys()
            if self.model != None:
                boxes = self.model.showLastResult()
            else:
                return None
            if boxes != None:
                clss = boxes[:, 5]
                count = Counter(clss.long().tolist())
                resultcounter = {str(k): v for k, v in count.items()}
                classes_count = {classes[int(k)]: v for k, v in resultcounter.items()}
                return classes_count
            else:
                return None

    def CountSquare(self,classes_in_shot:dict):
        classes:dict = self.kernel.kernel.names
        #print(classes)
        inv_classes = dict((v, k) for k, v in classes.items())
        result = dict()
        try:
            pic = self.model.showLastShot()
            width = len(pic[0])
            height = len(pic)
            boxes = self.model.showLastResult()
            masks = self.model.showLastSizes()
        except:
            print('No model found')
            return None
        
        if boxes!=None and masks!=None:
            clss = boxes[:, 5]
            exist_keys = list(classes_in_shot.keys())

            for key in exist_keys:
                item_indicies = torch.where(clss == inv_classes[key])
                item_masks = masks[item_indicies]
                item_mask = torch.any(item_masks,dim = 0).int() * 255
                image_mask = item_mask.cpu().numpy().astype('uint8')
                image_mask = cv2.resize(image_mask,(width,height))
                #cv2.imshow(image_mask)
                #cv2.waitKey(0)
                #print(len(image_mask))
                #print(len(image_mask[0]))

                cntw = cv2.countNonZero(image_mask)
                if self.onepixdim == 0:
                    result[key] = cntw
                else:
                    result[key] = cntw * self.onepixdim
                    #print('RJOMBA')
                    #print(self.onepixdim)
            return result
        else:
            print('No masks or boxes found')
            return None
        

    def change_confidence(self,value):
        self.model.confidence = value    
cont = controller()
