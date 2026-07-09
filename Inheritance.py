class Parent:
    def land(self):
        print("parent has 10acrs")
    def bus(self):
        print("Pushpak travels")
class Child(Parent):
    def bus(self):
        print("VRL Travels")
    def degree(self):
        print("B.Tech Degree")
class Child2(Parent):
    def land(self):
        print("1acr")
c = Child()
c2 = Child2()
c.bus()
c2.land()
