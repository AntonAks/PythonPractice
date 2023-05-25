class Car:
    # Class Variable
    car_count = 0

    def __init__(self, brand, model, color):
        # Instance Variables
        self.brand = brand
        self.model = model
        self.color = color
        Car.car_count += 1

    # Instance Method
    def drive(self):
        print(f"Driving the {self.color} {self.brand} {self.model}")

    # Class Method
    @classmethod
    def get_car_count(cls):
        return cls.car_count

    # Static Method
    @staticmethod
    def honk():
        print("Honk honk!")

# Creating instances of Car
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Accord", "Red")

# Calling instance method
car1.drive()  # Output: Driving the Blue Toyota Camry

# Calling class method
count = Car.get_car_count()
print("Total cars:", count)  # Output: Total cars: 2

# Calling static method
Car.honk()  # Output: Honk honk!


class ElectricCar(Car):
    def __init__(self, brand, model, color, battery_capacity):
        super().__init__(brand, model, color)
        self.battery_capacity = battery_capacity

    def drive(self):
        print(f"Driving the {self.color} {self.brand} {self.model} (Electric)")

    def charge(self):
        print(f"Charging the {self.brand} {self.model}...")


class HybridCar(Car):
    def __init__(self, brand, model, color, gas_tank_capacity):
        super().__init__(brand, model, color)
        self.gas_tank_capacity = gas_tank_capacity

    def drive(self):
        print(f"Driving the {self.color} {self.brand} {self.model} (Hybrid)")

    def refill_gas(self):
        print(f"Refilling gas for {self.brand} {self.model}...")

# Creating instances of ElectricCar and HybridCar
electric_car = ElectricCar("Tesla", "Model S", "Black", "100 kWh")
hybrid_car = HybridCar("Toyota", "Prius", "Silver", "11 gallons")

# Calling overridden methods
electric_car.drive()  # Output: Driving the Black Tesla Model S (Electric)
hybrid_car.drive()   # Output: Driving the Silver Toyota Prius (Hybrid)

# Calling additional methods
electric_car.charge()      # Output: Charging the Tesla Model S...
hybrid_car.refill_gas()    # Output: Refilling gas for Toyota Prius...
