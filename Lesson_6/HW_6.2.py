"""
Task 6.2
"""
class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.massa = 25
        self.visota = 5
    def asvalt_massa (self):
        return self._length * self._width * self.massa * self.visota

road = Road(5000, 20)
print(f'Понадобится {road.asvalt_massa()/1000} тонн асфальта')