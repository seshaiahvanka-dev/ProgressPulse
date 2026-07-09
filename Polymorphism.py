class Plane:
    def take_off(self):
        print("Plane is taking Off")
    def fly(self):
        print("Plane is flying")
    def land(self):
        print("Plane is landing")
class CargoPlane(Plane):
    def take_off(self):
        print("CargoPlane is taking Off")
    def fly(self):
        print("CargoPlane is flying")
    def land(self):
        print("CargoPlane is landing")
    def transfer(self):
        print("CargoPlane carries cargo")
class PassengerPlane(Plane):
    def take_off(self):
        print("PassengerPlane is taking Off")
    def fly(self):
        print("PassengerPlane is flying")
    def land(self):
        print("PassengerPlane is landing")
    def transfer(self):
        print("PassengerPlane carries Passengers")
class FighterPlane(Plane):
    def take_off(self):
        print("FighterPlane is taking Off")
    def fly(self):
        print("FighterPlane is flying")
    def land(self):
        print("FighterPlane is landing")
    def transfer(self):
        print("FighterPlane carries Weopons")
class Airport:
    def parking(self,ref):
        ref.take_off()
        ref.fly()
        ref.land()
        ref.transfer()
def main():
    c = CargoPlane()
    p = PassengerPlane()
    f = FighterPlane()
    a = Airport()
    a.parking(c)
    a.parking(p)
    a.parking(f)
    # c.take_off()
    # c.fly()
    # c.land()
    # c.transfer()
    # p.take_off()
    # p.fly()
    # p.land()
    # p.transfer()
    # f.take_off()
    # f.fly()
    # f.land()
    # f.transfer()
if __name__ == '__main__':
    main()