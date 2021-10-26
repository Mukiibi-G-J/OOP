# inheritance
class first1:
    def dog(self):
        print('This is a dog method')


class first2(first1):
    pass
    # def dog2 (self):
    #     print('This is a dog 2')


c = first2()
print(c.dog())


# Muilt level inheritance

class P:
    def m1(self):
        print("parent method")


class C(P):
    def m2(self):
        print('sub method')


class d(C):
    def m3(self):
        print('child class')


object = d()

object.m1()
object.m2()
object.m3()
