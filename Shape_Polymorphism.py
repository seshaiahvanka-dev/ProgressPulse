class Shape:
    def draw(self):
        print("Drawing a generic shape")
class Circle(Shape):
    def draw(self):
        print("Drawing a circle")
class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")
class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")
def geometry(ref):
    ref.draw()
s = [Circle(),Rectangle(),Triangle()]
for i in s:
    geometry(i)