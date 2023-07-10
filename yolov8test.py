from ultralytics import YOLO
import cv2
import torch
import numpy as np
# Load a model
model = YOLO('ourmodels/yolov8n-seg.pt')  # pretrained YOLOv8n model

# Run batched inference on a list of images
results = model('source/bottle.jpg')  # return a list of Results objects


print(model.names)


for result in results:
    # get array results
    masks = result.masks.data
    boxes = result.boxes.data
    # extract classes
    clss = boxes[:, 5]
    # get indices of results where class is 0 (people in COCO)
    people_indices = torch.where(clss == 39)
    # use these indices to extract the relevant masks
    people_masks = masks[people_indices]
    # scale for visualizing results
    people_mask = torch.any(people_masks, dim=0).int() * 255
    # save to file
    lol = people_mask.cpu().numpy().astype('uint8')
    print(people_mask.cpu().numpy().astype('uint8'))
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
    #cv2.imwrite(str(model.predictor.save_dir / 'merged_segs.jpg'), people_mask.cpu().numpy())
    cv2.imshow('pidor',lol)
    cv2.waitKey(0)
    '''
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
'''