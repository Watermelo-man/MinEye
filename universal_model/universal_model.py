from modelType import *

from kernel import *


#add different types here    
SelectModelbyInputAndKernel = fabric()
SelectModelbyInputAndKernel.addType("IMGPIL",modelIMGPIL)
SelectModelbyInputAndKernel.addType("LiveVideo",modelVideoCapture)
#... add another type
#add different types here


Kernel = kernel("models/onlygold.pt","cpu")

memodel = SelectModelbyInputAndKernel.selectModel(Kernel, "IMG")
print (type(memodel))



im =  PIL.Image.open("source/0010.jpg")


memodel.predict(im , 640, 0.5,0.5)

out = cv2.resize(memodel._show_last_result(),(640,480))

cv2.imshow('Noutput', out)
cv2.waitKey()

