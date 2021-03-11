from CarFactory.index import CarFactory
from Car.index import Car
from Client.index import Client
import json


class System:
    cars = []
    clients = []

    @classmethod
    def initialiseCarsData(cls, jsonPath):
        with open(jsonPath) as carsJson:
            carsData = json.load(carsJson)
        cls.cars = CarFactory.getCarList(carsData['cars'])

    @classmethod
    def run(cls):
        print("run")
        print("cars",cls.cars)
