
import yolov5


class kernel():    
    kernel:yolov5
    def __init__(self, model_path:str, device:str):
        self.kernel = yolov5.load(model_path, device)