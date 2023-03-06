import sys
from pathlib import Path
import universal_model 
import cv2
from PIL import Image
from PyQt6.QtGui import QPixmap, QImage




kernel = universal_model.kernel.kernel(model_path="C:\\Users\\Alexander\\Desktop\\orereco\\ourmodels\\yolov5n.pt", device="CPU")

#im = cv2.imread("C:\\Projects\\orereco\\source\\bottle.jpg")



#im = cv2.VideoCapture(0)

#md = universal_model.modelType.PictureModel(kernel.kernel)
#md = universal_model.modelType.VideoModel(kernel.kernel)




def selectType(type:int):
    if type == 1:
        md = universal_model.modelType.models.selectModel(kernel.kernel, "PictureModel")
        return md
    elif type == 2:
        md == universal_model.modelType.models.selectModel(kernel.kernel, "VideoModel")
    else:
        return -1
    
md = selectType(1)

    
im =Image.open("C:\\Users\\Alexander\\Desktop\\orereco\\source\\bottle.jpg")



def analyseShot(model:universal_model.modelType.Imodel = md,im = im):
    model.predict(im)
    res= md.showLastShot()
    #create from numpy Qpixmap
    h,w,ch = res.shape
    bytes_per_line = ch*w
    convert_to_Qt_format = QImage(res.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
    #create from numpy Qpixmap
    return convert_to_Qt_format








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
 