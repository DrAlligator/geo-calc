import math

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.width = width
        self.__area = self.__length * self.width
        self.__perimeter = self.__length * 2 + self.width * 2
        self.__diagonal = math.sqrt(math.pow(self.__length, 2) + math.pow(self.width, 2))

    def get_area(self):
        return self.__area

    def get_perimeter(self):
        return self.__perimeter

    def get_diagonal(self):
        return self.__diagonal