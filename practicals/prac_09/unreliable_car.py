from car import Car
import random

class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance if it is reliable enough."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
    def __str__(self):
        return f"{super().__str__()}, Reliability: {self.reliability}%"





