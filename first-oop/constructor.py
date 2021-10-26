# class Computer:
#     pass

# c1 = Computer()
# c2 = Computer()
# print(id(c1))
# print(id(c2))


class Computer:

    def __init__(self):
        self.name = "Mukiibi"
        self.age = 45

    def upgrade(self):
        self.name = 60

    def compair(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c3 = Computer()
c4 = Computer()
c3.name = "John"
c3.age = 78
if c4.compair(c3):
    print("they are the same")
else:
    print("they are different")
print(c4.upgrade())
print(c3.name)
print(c3.age)
