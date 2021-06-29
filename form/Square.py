import math

class Square:
    def __init__(self, length):
        self.__length = length
        self.__area = math.pow(self.__length, 2)
        self.__perimeter = self.__length * 4
        self.__diagonal = math.sqrt(self.__length * 2)

    def get_area(self):
        return self.__area

    def get_perimeter(self):
        return self.__perimeter

    def get_diagonal(self):
        return self.__diagonal