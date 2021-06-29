import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__circumference = self.__radius * 2 * math.pi
        self.__area = math.pi * math.pow(self.__radius, 2)

    def get_circumference(self):
        return self.__circumference

    def get_area(self):
        return self.__area
