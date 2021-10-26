class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def diplay(self):
        print('Hi', self.name)
        print('Your marks are', self.marks)

    def grade(self):
        if self.marks >= 60:
            print('Your marks is', self.marks)
        elif self.marks >= 50:
            print('Your have second grade')
        else:
            print('failed')


firstObject = Student('Mukiibi', 56)

print(firstObject.diplay())

print(firstObject.grade())
