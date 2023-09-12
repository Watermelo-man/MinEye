from ultralytics import YOLO
import cv2
import torch
import numpy as np
# Load a model
model = YOLO('ourmodels/yolov8n-seg.pt')  # pretrained YOLOv8n model
classes = model.names
print(classes)
# Run batched inference on a list of images
results = model('source/7c98d4e3207fa8b44c42122ca7da455f.jpg')  # return a list of Results objects

image = cv2.imread('source/7c98d4e3207fa8b44c42122ca7da455f.jpg')
height, width, channels = image.shape
print(height,width)
print()
cv2.imshow('huila',image)
#print(model.names)s


for result in results:
    # get array results
    masks = result.masks.data
    boxes = result.boxes.data
    # extract classes

    print( result.masks.data)
    clss = boxes[:, 5]
    print (clss)
    # get indices of results where class is 0 (people in COCO)
    people_indices = torch.where(clss == 39)
    # use these indices to extract the relevant masks
    people_masks = masks[people_indices]
    print(type(people_masks))
        # scale for visualizing results
    people_mask = torch.any(people_masks,dim = 0).int() * 255

    #people_mask =  people_masks.cpu().numpy()
    # save to file
    lol = people_mask.cpu().numpy().astype('uint8')
    lol = cv2.resize(lol,(width,height))
   # cv2.imshow('kekoch',resized)
   # cv2.waitKey(0)
    
    #print(people_mask.cpu().numpy().astype('uint8'))
    cnt = 0
    cntb = 0
    for row in lol:
        for pix in row:
            if pix != 0:
                cnt +=1
            else:
                cntb += 1
    print(cnt)
    print(cntb)
    #print(len(lol))
    #print(len(lol[0]))
    #print(sum(sum(lol)))
    #cv2.imwrite(str(model.predictor.save_dir / 'merged_segs.jpg'), people_mask.cpu().numpy())
    cv2.imshow('pidor',lol)
    #cv2.imshow('pidor2',results)
    cv2.waitKey(0)
    
# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bbox outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Class probabilities for classification outputs
print(masks)
res_plotted = results[0].plot()
cv2.imshow("result", res_plotted)
cv2.waitKey(0)