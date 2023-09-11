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
    kernel = None
    mode_type = None
    def __init__(self, model_path = './ourmodels/yolov8n.pt', auto:bool = True, device:str = 'cpu'):
        #self.kernel = torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cuda() # local repo
        #dev = torch.device('cuda:0')
        #print(torch.cuda.is_available())
        
        if auto:

            if self.mode_type != None:
                if  self.mode_type == 'cuda':
                    model = YOLO(model_path)
                    #model = model.export()
                    self.kernel = model(device = 0)#torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cuda()
                    #self.kernel
                    print("CUDA MODE")
                if  self.mode_type == 'cpu':
                    model = YOLO(model_path)
                    #model = model.export(format = 'ONNX')
                    #model = model.export()
                    self.kernel = model#torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cpu()   
                    print("CPU MODE")


            if torch.cuda.is_available() and self.mode_type == None:
                answ = input('There is some CUDA, do you want to use it?(Y/N)')
                if answ == 'Y':
                    self.mode_type = 'cuda'
                    model = YOLO(model_path)
                    #model = model.export()
                    self.kernel = model(device = 0)#torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cuda()
                    #self.kernel
                    print("CUDA MODE")
                else:
                    self.mode_type = 'cpu'
                    model = YOLO(model_path)
                    #model = model.export(format = 'ONNX')
                    #model = model.export()
                    self.kernel = model#torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cpu()   
                    print("CPU MODE")
            

    def change_model(self,model_path):
        if  self.mode_type == 'cuda':
            model = YOLO(model_path)
            #model = model.export()
            self.kernel = model(device = 0)#torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cuda()
            #self.kernel
            print("CUDA MODE")
        if  self.mode_type == 'cpu':
            model = YOLO(model_path)
            #model = model.export(format = 'ONNX')
            #model = model.export()
            self.kernel = model#torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True).cpu()   
            print("CPU MODE")
        #else:  

kernelinst = kernel()

        #self.kernel = torch.hub.load(yolodir, 'custom', path = model_path, source='local', force_reload=True)
    #def getkernel(self):
     #   return self.__kernel


