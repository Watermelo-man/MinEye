from pathlib import Path
import universal_model 
import cv2
from PIL import Image
from PyQt6.QtGui import QImage
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
            else:
                self.selectType(1)
                self.source = Image.open(str(self.path))
            return 0
        elif src == 2:
            self.selectType(2)
            self.source = cv2.VideoCapture(0, cv2.CAP_DSHOW)
            return 0
        else:
            return -1
        
    
    def analyseShot(self):#(model:universal_model.modelType.Imodel = md,im = im):
        self.model.predict(self.source)
        self.res = self.model.showLastShot()
        h,w,ch = self.res.shape
        bytes_per_line = ch*w
        convert_to_Qt_format = QImage(self.res.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        return convert_to_Qt_format
    

cont = controller()
 