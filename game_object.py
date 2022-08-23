import os
import engine, images, error
import pygame

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# g * m

class Transform(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = None
        self.physics = False
        self.collider = False
        self.speed = 2
        self.weight = 0.1 # kilograms
        self.gravity = self.weight * 7
        self.name = None
        self.tag = None
        print(self.gravity)

    def DoBeforeUpdate(self):
        pass