class Vehicle:
    def __init__(self, type, wheels=True, engine=True):
        self.type = type
        self.wheels = wheels
        self.engine = engine

    def get_type(self):
        return f'This vehicle is a {self.type}'


class Car(Vehicle):
    def __init__(self, brand, color, type='car'):
        self.brand = brand
        self.color = color
        super().__init__(type)


class Truck(Vehicle):
    def __init__(self, brand, color, type='truck'):
        self.brand = brand
        self.color = color
        super().__init__(type)
