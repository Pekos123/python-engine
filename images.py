import cv2
from PIL import Image as _image

class Image:
    def __init__(self, path, scale = (1, 1)):
        self.path = path
        self.scale = scale
        self.image = cv2.imread(self.path)

class Sprite(Image):
    def __init__(self, path, scale = (1, 1)):
        super().__init__(path, scale)
        self.x = 0
        self.y = 0
        self.imagepill = _image.open(self.path)
        self.width = int(self.imagepill.width * self.scale[0])
        self.height = int(self.imagepill.height * self.scale[1])
        
        self.image = cv2.resize(self.image, (self.width, self.height))