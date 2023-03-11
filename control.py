import sys
from pathlib import Path
import universal_model 
import cv2
from PIL import Image
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QFileDialog
from enum import Enum

class types(Enum):
    photo = 1
    video = 2


class controller():
    model = None
    source = None
    kernel = None
    def __init__(self):
         self.kernel = universal_model.kernel.kernel(model_path=r"C:\Users\Acer\Desktop\orereco\orereco\ourmodels\yolov5n.pt", device="CPU")
         
    def selectType(self,type:int):
        if type == 1:
            self.model = universal_model.modelType.models.selectModel(self.kernel.kernel, "PictureModel")
            return 0
        elif type == 2:
            self.model == universal_model.modelType.models.selectModel(self.kernel.kernel, "VideoModel")
            return 0
        else:
            return -1
    
    def selectSource(self,src:int = 1):
        if src == 1:
            #self.source = Image.open("C:/Users/Alexander/Desktop/orereco/source/bottle.jpg")
            path,check = QFileDialog.getOpenFileName(None, "Open Image","","Image Files (*.png *.jpg)")
            self.source = Image.open(str(path))
            return 0
        elif src == 2:
            self.source ==cv2.VideoCapture(0)
            return 0
        else:
            return -1
    
    def analyseShot(self):#(model:universal_model.modelType.Imodel = md,im = im):
        print(self.source)
        self.model.predict(self.source)
        res= self.model.showLastShot()
        #create from numpy Qpixmap
        h,w,ch = res.shape
        bytes_per_line = ch*w
        convert_to_Qt_format = QImage(res.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        #create from numpy Qpixmap
        return convert_to_Qt_format


cont = controller()
cont.selectType(1)
#cont.selectSource()






'''
while(True):
    

    md.predict(im)

    res = md.showLastShot()


    cv2.imshow("lol",cv2.resize(res,[640,480]))#cv2.resize(res,[640,480]))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#cv2.waitKey(0)
'''

"""
from universal_model import kernel
from universal_model import modelType

"""
 