from CarFactory.index import CarFactory
from Car.index import Car
from Client.index import Client
import json

class System:

    @staticmethod
    def run():
        myJsonFile = open('carsList.json', 'r')
        dataJson = myJsonFile.read()
        print("System")
        print(dataJson)
