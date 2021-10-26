# An example
# if you add
# 5 + 5 = 10              This can be know as
# r + t  = rt              operate overloading

# polymorphism is means may forms


class Product:

    def m1(self, *a):
        total = 0
        for X in a:
            total = X+1
            print(total)


c1 = Product()
print(c1.m1(10))
print(c1.m1(10, 45))
print(c1.m1(10, 46, 46, 46))
print(c1.m1(10, 454, 54, 54, 545))
