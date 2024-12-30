class ColoredPoint:
    def __init__(self, x, y, color):
        self.__x = x
        self.__y = y
        self.__color = color

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def color(self):
        return self.__color

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return (self.__x, self.__y, self.__color) == (other.__x, other.__y, other.__color)

        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, ColoredPoint):
            return not((self.__x, self.__y, self.__color) == (other.__x, other.__y, other.__color))

        return NotImplemented

    def __hash__(self):
        return hash((self.__x, self.__y, self.__color))

    def __str__(self):
        return f"ColoredPoint({self.__x}, {self.__y}, '{self.__color}')"


point1 = ColoredPoint(1, 2, "red")
point2 = ColoredPoint(1, 2, "red")
point3 = ColoredPoint(2, 3, "blue")

print(point1 == point2)
print(point1 != point3)

points_dict = {point1: "First point", point3: "Second point"}
print(points_dict[point1])

print(point1)