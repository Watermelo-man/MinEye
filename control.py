import sys
from pathlib import Path
import universal_model 
import cv2
from PIL import Image
from PyQt6.QtGui import QPixmap, QImage


class controller():
    model = None
    source = None
    kernel = None
    def __init__(self):
         self.kernel = universal_model.kernel.kernel(model_path="C:\\Users\\Alexander\\Desktop\\orereco\\ourmodels\\yolov5n.pt", device="CPU")
    
    def selectType(self,type:int):
        if type == 1:
            self.model = universal_model.modelType.models.selectModel(self.kernel.kernel, "PictureModel")
            return 0
        elif type == 2:
            self.model == universal_model.modelType.models.selectModel(self.kernel.kernel, "VideoModel")
            return 0
        else:
            return -1
    
    def selectSource(self,src:int):
        if src == 1:
            self.source = Image.open("C:\\Users\\Alexander\\Desktop\\orereco\\source\\bottle.jpg")
            print(type(self.source))
            return 0
        elif src == 2:
            self.source ==cv2.VideoCapture(0)
            return 0
        else:
            return -1
    
    def analyseShot(self):#(model:universal_model.modelType.Imodel = md,im = im):
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
cont.selectSource(1)






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
 