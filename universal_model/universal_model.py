from modelType import *

from kernel import *


#create fabric
SelectModelbyInputAndKernel = fabric() 
#add different types here    
SelectModelbyInputAndKernel.addType("IMGPIL",modelIMGPIL)
SelectModelbyInputAndKernel.addType("LiveVideo",modelVideoCapture)
#... add another type
#add different types here


Kernel = kernel("C:/Projects/orereco/ourmodels/yolov5x.pt","cuda:0")

memodel = SelectModelbyInputAndKernel.selectModel(Kernel, "LiveVideo")
print (type(memodel))



#im =  PIL.Image.open("source/0010.jpg")
im = cv2.VideoCapture(0)





while(True):
    memodel.predict(im , 640, 0.3,0.3)


    out = cv2.resize(memodel._show_last_result(),(640,480))
    cv2.imshow('Noutput', out)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
im.release()

cv2.waitKey()

