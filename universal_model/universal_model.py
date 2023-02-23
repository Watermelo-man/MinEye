from modelType import *

from kernel import *


#create fabric
SelectModelbyInputAndKernel = fabric() 
#add different types here    
SelectModelbyInputAndKernel.addType("IMGPIL",modelIMGPIL)
SelectModelbyInputAndKernel.addType("LiveVideo",modelVideoCapture)
#... add another type
#add different types here


Kernel = kernel("C:/Projects/orereco/ourmodels/onlygold.pt","cpu")

memodel = SelectModelbyInputAndKernel.selectModel(Kernel, "IMGPIL")
print (type(memodel))



im =  PIL.Image.open("source/0010.jpg")


memodel.predict(im , 640, 0.5,0.5)

out = cv2.resize(memodel._show_last_result(),(640,480))

cv2.imshow('Noutput', out)
cv2.waitKey()

