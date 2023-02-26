import torch
import cv2
import time
import numpy 
import torchvision.transforms.functional as F



class kernel():
   kernel=None
   def __init__(self, model_path = 'C:/Projects/orereco/ourmodels/yolov5x.pt', device:str = 'CUDA:0'):
        self.kernel = torch.hub.load('./yolov5', 'custom', path = model_path, source='local',device=device)  # local repo

#kek = kernel()
"""
ker = kernel()


#im = cv2.cvtColor(cv2.imread("C:/Projects/orereco/source/0038.jpg"), cv2.COLOR_BGR2RGB)

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