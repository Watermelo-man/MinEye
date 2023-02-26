from modelType import *

from kernel import *

from ultralytics import YOLO

import sys

#create fabric
SelectModelbyInputAndKernel = fabric() 
#add different types here    
SelectModelbyInputAndKernel.addType("IMGPIL",modelIMGPIL)
SelectModelbyInputAndKernel.addType("LiveVideo",modelVideoCapture)
#... add another types
#add different types here

Kernel = kernel("ourmodels/onlygold.pt","cuda:0")

testModel = SelectModelbyInputAndKernel.selectModel(Kernel, "IMGPIL")


im =  PIL.Image.open("source/0038.jpg")
#im = cv2.VideoCapture(0)


testModel.predict(im , 640, 0.3,0.3)
# while(True):

out = cv2.resize(cv2.cvtColor(testModel._show_last_result(), cv2.COLOR_BGR2RGB),(640,480))
print (testModel.last_result_data().xyxy[0])


cv2.imshow('Noutput', out)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

cv2.waitKey(0)

im.release()