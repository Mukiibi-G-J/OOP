class Polygon:
    __height = None
    __Width = None

    def set_Values(self, width, height):
        self.__Width = width
        self.__height = height

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__Width


class Square(Polygon):
    def area(self):
        return self.get_width()*self.get_height()


class Triangel(Polygon):
    def area(self):
        return self.get_width() * self.get_height() * 1/2


s1 = Square()
s1.set_Values(9, 12)
print(s1.area())


s2 = Triangel()
s2.set_Values(9, 12)

print(s2.area())
