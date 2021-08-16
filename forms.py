import math
import matplotlib.pyplot as plt



class Circle:
    def __init__(self, radius):
        """initiate class Circle with radius and calculates the circumference and Circlearea

        Args:
            radius (float): Circle radius
        """
        self.__radius = radius

    def get_circumference(self):
        """get the circumference of the Circle

        Returns:
            float: circle circumference
        """
        return self.__radius * 2 * math.pi

    def get_area(self):
        """get the area of the circle

        Returns:
            float: circle area
        """
        return math.pi * math.pow(self.__radius, 2)

    def show(self):
        """will show a graph with a circle with the radius given in the init
        """
        figure, axes = plt.subplots()
        draw_circle = plt.Circle((self.__radius * 1.1, self.__radius * 1.1), self.__radius)

        axes.set_xlim((0, self.__radius*2.2))
        axes.set_ylim((0, self.__radius*2.2))
        axes.set_aspect(1)
        axes.add_artist(draw_circle)
        plt.title("Circle")
        plt.show()
        plt.clf()

class Square:
    def __init__(self, square_length):
        """initiate class Square and calculates the area, perimeter and the diagonal with the given lenght

        Args:
            square_length (float): side length of the square
        """
        self.__square_length = square_length

    def get_area(self):
        """gives the area of the square

        Returns:
            float: square area
        """
        return math.pow(self.__square_length, 2)

    def get_perimeter(self):
        """gives the perimeter of the square

        Returns:
            float: perimeter of the square
        """
        return self.__square_length * 4

    def get_diagonal(self):
        """gives the diagonal of the square

        Returns:
            float: square diagonal
        """
        return math.sqrt(self.__square_length * 2)

    def show(self):
        """will show a graph with a square of the given side length
        """
        figure, axes = plt.subplots()
        draw_square = plt.Rectangle((self.__square_length * 0.1, self.__square_length * 0.1), self.__square_length, self.__square_length)

        axes.set_xlim((0, self.__square_length*1.2))
        axes.set_ylim((0, self.__square_length*1.2))
        axes.set_aspect(1)
        axes.add_artist(draw_square)
        plt.title("Square")
        plt.show()
        plt.clf()

class Rectangle:
    def __init__(self, rectangle_length, rectangle_width):
        """initiates class Rectangle and calculates the area, perimeter and diagonal with the given sides

        Args:
            rectangle_length (float): rectangle length
            rectangle_width (float): rectangle width
        """
        self.__rectangle_length = rectangle_length
        self.__rectangle_width = rectangle_width

    def get_area(self):
        """returns the area of the rectangle

        Returns:
            float: rectangle area
        """
        return self.__rectangle_length * self.__rectangle_width

    def get_perimeter(self):
        """returns the perimeter of the rectangle

        Returns:
            float: rectangle perimeter
        """
        return self.__rectangle_length * 2 + self.__rectangle_width * 2

    def get_diagonal(self):
        """returns the diagonal of the rectangle

        Returns:
            float: rectangel diagonal
        """
        return math.sqrt(math.pow(self.__rectangle_length, 2) + math.pow(self.__rectangle_width, 2))

    def show(self):
        """will show will show a graph with a rectangle of the given sides
        """
        figure, axes = plt.subplots()
        draw_rectangle = plt.Rectangle((self.__rectangle_length * 0.1, self.__rectangle_width * 0.1), self.__rectangle_length, self.__rectangle_width)

        axes.set_xlim((0, self.__rectangle_length*1.2))
        axes.set_ylim((0, self.__rectangle_width*1.2))
        axes.set_aspect(1)
        axes.add_artist(draw_rectangle)
        plt.title("Rectangle")
        plt.show()
        plt.clf()