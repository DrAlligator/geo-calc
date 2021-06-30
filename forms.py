import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
        self.__circumference = self.__radius * 2 * math.pi
        self.__circle_area = math.pi * math.pow(self.__radius, 2)

    def get_circumference(self):
        return self.__circumference

    def get_area(self):
        return self.__circle_area

class Square:
    def __init__(self, square_length):
        self.__square_length = square_length
        self.__square_area = math.pow(self.__square_length, 2)
        self.__square_perimeter = self.__square_length * 4
        self.__square_diagonal = math.sqrt(self.__square_length * 2)

    def get_area(self):
        return self.__square_area

    def get_perimeter(self):
        return self.__square_perimeter

    def get_diagonal(self):
        return self.__square_diagonal

class Rectangle:
    def __init__(self, rectangle_length, rectangle_width):
        self.__rectangle_length = rectangle_length
        self.__rectangle_width = rectangle_width
        self.__rectangle_area = self.__rectangle_length * self.__rectangle_width
        self.__rectangle_perimeter = self.__rectangle_length * 2 + self.__rectangle_width * 2
        self.__rectangle_diagonal = math.sqrt(math.pow(self.__rectangle_length, 2) + math.pow(self.__rectangle_width, 2))

    def get_area(self):
        return self.__rectangle_area

    def get_perimeter(self):
        return self.__rectangle_perimeter

    def get_diagonal(self):
        return self.__rectangle_diagonal