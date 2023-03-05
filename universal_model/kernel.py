import torch
import cv2
import numpy 
#mport torchvision.transforms.functional as F
#import pathlib

import os
rootdir = str(os.path.dirname(os.path.abspath(__file__)))
#yolodir = str(pathlib.Path.cwd())+'\\yolov5'
#yolodir = str(os.path.abspath("yolov5"))+'\\yolov5'

yolodir = rootdir + "\\yolov5"

print(yolodir)
class kernel():
    kernel=None
    def __init__(self, model_path = './orereco/ourmodels/yolov5n.pt', device:str = 'CPU'):
        self.kernel = torch.hub.load(yolodir, 'custom', path = model_path, source='local',device=device)  # local repo
    #def getkernel(self):
     #   return self.__kernel



"""
ker = kernel()


im = cv2.cvtColor(cv2.imread("C:/Users/Alexander/Desktop/orereco/source/bottle.jpg"), cv2.COLOR_BGR2RGB)

print(type(im))

cum = cv2.VideoCapture(0)

while(True):
    ret, shot = cum.read()

#im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    shot = cv2.cvtColor(shot,cv2.COLOR_BGR2RGB)
    res = ker.kernel(shot)
    #print (res.render()[0])
    #out = res.detach().cpu().numpy()
    #res.show()
    cv2.imshow("kek",cv2.cvtColor(res.render()[0], cv2.COLOR_RGB2BGR) )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #print(res)
"""