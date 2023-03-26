import torch
import cv2
import numpy 
#mport torchvision.transforms.functional as F
#import pathlib

import os
rootdir = str(os.path.dirname(os.path.abspath(__file__)))

#yolodir = rootdir + "\\yolov5"

yolodir = os.path.join(rootdir,'yolov5')

print(yolodir)
class kernel():
    __slots__ = "kernel",
    
    def __init__(self, model_path = './orereco/ourmodels/yolov5n.pt', device:str = 'CPU'):
        self.kernel = torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cuda() # local repo
    #def getkernel(self):
     #   return self.__kernel


