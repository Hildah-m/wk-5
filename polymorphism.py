class Vehicle:
    def move(self):
        pass  # Placeholder for the move method, to be defined in subclasses

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Create instances of each subclass
car = Car()
plane = Plane()

# Polymorphism in action
car.move()    # Outputs: Driving 🚗
plane.move()  # Outputs: Flying ✈️
