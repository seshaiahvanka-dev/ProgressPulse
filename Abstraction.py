from abc import ABC,abstractmethod


class Shape(ABC):
    def __init__(self):
        self.area = 0

    @abstractmethod
    def takeinput(self):
        pass

    @abstractmethod
    def calarea(self):
        pass

    @abstractmethod
    def disparea(self):
        pass

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.r =0

    def takeinput(self):
        self.r = int(input('Enter Radius: \n'))

    def calarea(self):
        self.area = 3.142*self.r**2

    def disparea(self):
        print('Circle Area:',self.area)

class Rectangle(Shape):
    def __init__(self):
        self.l =0
        self.b=0
        super().__init__()

    def takeinput(self):
        self.l = int(input('Enter the length:\n'))
        self.b = int(input('Enter the breadth:\n'))

    def calarea(self):
        self.area = self.l*self.b

    def disparea(self):
        print(f'Rectangle Area:{self.area}')

class Triangle(Shape):
    def __init__(self):
        super().__init__()
        self.b = 0
        self.h =0

    def takeinput(self):
        self.b = int(input('Enter the base:\n'))
        self.h = int(input('Enter the height:\n'))

    def calarea(self):
        self.area = (self.h*self.b)/2

    def disparea(self):
        print(f'Triangle Area:{self.area}')

def geometry(ref):
    ref.takeinput()
    ref.calarea()
    ref.disparea()

def main():
    c = Circle()
    r = Rectangle()
    t = Triangle()
    geometry(c)
    geometry(r)
    geometry(t)
    
if __name__ == '__main__':
    main()