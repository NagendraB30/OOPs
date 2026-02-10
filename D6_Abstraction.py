from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass  # Abstract methods have no body

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started: Vroom Vroom")

class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started: KICK START")

class Bus(Vehicle):
    def start_engine(self):
        print("Bus engine started: Heavy sound")

car_obj = Car()
bike_obj = Bike()
bus_obj = Bus()

car_obj.start_engine()
bike_obj.start_engine()
bus_obj.start_engine()