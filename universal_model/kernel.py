from ultralytics import YOLO
import torch
import cv2
import numpy 
#mport torchvision.transforms.functional as F
#import pathlib

import os
rootdir = str(os.path.dirname(os.path.abspath(__file__)))

#yolodir = rootdir + "\\yolov5"

yolodir = os.path.join(rootdir,'ultralytics')

print(yolodir)
class kernel():
    __slots__ = "kernel",
    
    def __init__(self, model_path = './orereco/ourmodels/yolov8n.pt', auto:bool = True, device:str = 'cpu'):
        #self.kernel = torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cuda() # local repo
        #dev = torch.device('cuda:0')
        #print(torch.cuda.is_available())
        if auto:
            if torch.cuda.is_available():
                model = YOLO(model_path)
                model = model.export()
                self.kernel = model#torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cuda()
                #self.kernel
                print("CUDA MODE")
            else:
                model = YOLO(model_path)
                #model = model.export()
                self.kernel = model#torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cpu()   
                print("CPU MODE")
        #else:

        #self.kernel = torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True)
    #def getkernel(self):
     #   return self.__kernel


