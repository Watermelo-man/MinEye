import cv2
import numpy as np
import torch


print(torch.cuda.is_available())


# print(torch.cuda.current_device())

# print(torch.cuda.get_device_name(0))

# import torchvision

# print(torchvision.__version__)
# print(torch.__version__)

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     cv2.imshow('video feed', frame)
    
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
        
# cap.release()
# cv2.destroyAllWindows()