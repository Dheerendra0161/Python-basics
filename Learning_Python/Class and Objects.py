class car:
    # Constructor (initializer) method
    def __init__(self, car_name, car_model, car_speed):
        # Instance attributes
        self.car_name = car_name
        self.car_speed = car_speed
        self.car_model = car_model

    # Instance method
    def cars_sale(self):
        print(f"{self.car_name} model {self.car_model} have speed {self.car_speed}")


# Creating instances of the Car class
car1 = car("Toyota", "Camry", 180)
car2 = car("Tesla", "Model 3", 210)

# Calling methods
car1.cars_sale()
car2.cars_sale()

# Accessing attributes
print(car1.car_name)
print(car2.car_model)

# Accessing class attribute
