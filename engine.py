import game_object, images, error
import os
import cv2

class Engine:
    def __init__(self):
        self.collisions_objects = []
        self.transforms = []


class Physics(Engine):
    def __init__(self):
        super().__init__()
        self.transforms_with_phycics = self.GetPhycicsTransforms()
        self.transforms_with_colliders = self.GetCollidersTranforms()

    def GetPhycicsTransforms(self):
        array = []
        for i in self.transforms:
            if i.phycics == True:
                array.append(i)

        return array if len(array) > 0 else None

    def GetCollidersTranforms(self):
        array = []
        for i in self.transforms:
            if i.collider == True:
                array.append(i)
        
        return array if len(array) > 0 else None


    def AffectToGravity(self):
        for transform in self.transforms:
            if transform.physics == True:
                if transform.sprite != None:
                    if self.Collision(transform):
                        pass
                    else:
                        transform.y += transform.gravity
                    transform.sprite.y = transform.y
                else:
                    error.MissingSprite(f"The Transform object {transform.name} #{transform.tag} dont have sprite. Add one by writing `transfromobj.sprite = sprite` before game loop")
                    os._exit(0)

    
    def Collision(self, transform):
        for i in self.transforms_with_colliders:
            if transform.x >= i.x and transform.x <= i.x + i.width and transform.y >= i.y and transform.y <= i.y + i.height:
                
                print(f"COLLISION {transform.name} with {transform.name}")
                return True
        return False


class Display:
    def __init__(self, x, y, caption = "Engine"):
        self.caption = caption

        self.width = x
        self.height = y

        self.window = cv2.namedWindow(self.caption, cv2.WINDOW_AUTOSIZE)
        self.background = cv2.imread("background.png")

        cv2.resizeWindow(self.caption, self.width, self.height)

    def draw(self, image : images.Sprite):
        if type(image) != images.Sprite:
            error.WrongType("[001] Your parrametr in method draw() isnt Sprite type.")
            print(type(image))
            os._exit(0)
        else:
            cv2.imshow(self.caption, image.image)

    def update(self):
        cv2.cvtColor(self.background, cv2.COLOR_BGR2GRAY)
        self.background = cv2.resize(self.background, (self.width, self.height))
        cv2.imshow(self.caption, self.background)
        # Nie moge ciągle odświerzać obrazu bo mi się okno wiesza
        cv2.waitKey(0)
        # bruh 
