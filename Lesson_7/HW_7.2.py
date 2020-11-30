"""
Task 7.2 # Николай, мне не нравится, что получилось, но большего я выжать не смог...
"""
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, V, H):
        self.V = V
        self.H = H

    @property
    def property_train (self):
        return print(f' Расход ткани составит: {(self.V / 6.5 + 0.5) +  (2 * self.H + 0.3)}')

@abstractmethod
def rashod(self):
    pass

class Coat(Clothes):
    def rashod (self):
        return print(f' Расход ткани на пальто составит: {self.V / 6.5 + 0.5}')

class Suit(Clothes):
    def rashod (self):
        return print(f' Расход ткани на костюмы составит: {2 * self.H + 0.3}')

CL = Clothes(500, 100)
CL.property_train
c = Coat(500, 100)
c.rashod()
s = Suit(500, 100)
s.rashod()