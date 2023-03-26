import sys
from pathlib import Path
import universal_model 
import cv2
from PIL import Image
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QFileDialog
from enum import Enum
import os
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes

class types(Enum):
    photo = 1
    video = 2


class controller():
    model = None
    source = None
    kernel = None
<<<<<<< Updated upstream
    def __init__(self,pth:str):
        #self.kernel = universal_model.kernel.kernel(model_path=r"C:\Projects\orereco\ourmodels\yolov5x.pt", device="CPU")
        self.kernel = universal_model.kernel.kernel(model_path=pth, device="CPU")
=======
    __currentType = types.photo

    __modelpth = str(os.path.dirname(os.path.abspath(__file__)))

    __modelpth = os.path.join(__modelpth,'ourmodels')

    __modelpth = os.path.join(__modelpth,'yolov5x.pt')

    #__modelpth = r"C:\Projects\orereco\ourmodels\yolov5x.pt"

    def __init__(self):
         self.kernel = universal_model.kernel.kernel(model_path=self.__modelpth, device="CUDA:0")

>>>>>>> Stashed changes
         
    def changeModelPath(self,pth:str)->None:
        self.__modelpth = pth
        self.kernel = universal_model.kernel.kernel(model_path=self.__modelpth, device="CUDA:0")
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
                self.source = cv2.VideoCapture(str(self.path))
                self.__currentType = 2
            else:
                self.selectType(1)
                self.source = Image.open(str(self.path))
                self.__currentType = 1
            return 0
        elif src == 2:
            self.selectType(2)
<<<<<<< Updated upstream
            self.source = cv2.VideoCapture(0)
=======
            self.source = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            self.__currentType = 2
>>>>>>> Stashed changes
            return 0
        else:
            return -1
        
    
    def analyseShot(self):#(model:universal_model.modelType.Imodel = md,im = im):
        self.model.predict(self.source)
        self.res = self.model.showLastShot()
        #create from numpy Qpixmap
        h,w,ch = self.res.shape
        bytes_per_line = ch*w
        convert_to_Qt_format = QImage(self.res.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        #create from numpy Qpixmap
        return convert_to_Qt_format
    

pth = os.path.join(str(os.path.dirname(os.path.abspath(__file__))) , "ourmodels")

pthall = os.path.join(pth,"yolov5x.pt")


def createContInstance(pth:str):
    global pthall
    print(pth)
    #contInstance = controller(pth)
    #print(contInstance)
    pthall = pth


contInstance = controller(pthall)
'''
pth = os.path.join(str(os.path.dirname(os.path.abspath(__file__))) , "ourmodels")

pthall = os.path.join(pth,"yolov5x.pt")


contInstance  = controller( pthall)


def createContInstance(pth:str):
    global contInstance
    print(pth)
    contInstance = controller(pth)
    print(contInstance)
'''