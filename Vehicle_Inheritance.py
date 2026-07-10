class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name = name
        self.max_speed = max_speed
        self.milage = milage
    def drive(self):
        print("Vehicle is being Driven")
    def display_info(self):
        print(self.name)
        print('Max Speed:',self.max_speed)
        print('Milage:',self.milage)
class Car(Vehicle):
    def __init__(self,name,max_speed,milage,doors):
        super().__init__(name,max_speed,milage)
        self.doors = doors
    def drive(self):
        print('Car is being Driven')
class Bus(Vehicle):
    def __init__(self,name,max_speed,milage,capacity):
        super().__init__(name,max_speed,milage)
        self.capacity = capacity
    def drive(self):
        print('Bus is being Driven')
    def fare(self):
        print('Total Fare:',self.capacity*10)
def garage(ref):
    ref.drive()
    ref.display_info()
    if type(ref) == Bus:
        ref.fare()
# v = Vehicle('Generic Vehicle',120,15)
# c = Car('Sedan',180,12,4)
# b = Bus('School Bus',100,8,50)
# garage(v)
# garage(c)
# garage(b)

def main():
    garage(Vehicle('Generic Vehicle',120,15))
    garage(Car('Sedan',180,12,4))
    garage(Bus('School Bus',100,8,50))

# v.drive()
# v.display_info()
# c.drive()
# c.display_info()
# b.drive()
# b.display_info()
# b.fare()

if __name__ == '__main__':
    main()