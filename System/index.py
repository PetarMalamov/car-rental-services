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
    def createClient(cls, clientData):
        print(clientData)

    @classmethod
    def printCars(cls):
        for car in cls.cars:
            car.printCar()

    @classmethod
    def getClient(cls):
        egnFromInput = input("Enter client egn: ")
        currentClient = None
        for client in cls.clients:
            if client.getEgn() == egnFromInput:
                print("here")
                currentClient = client
                break

        if currentClient is None:
            print("No client Found")
            print("Please add client to the system")
            newClient = input("Enter person first name, last name, egn: ")
            currentClient = Client.from_strings(newClient)
            cls.clients.append(currentClient)

        currentClient.print()
        return currentClient

    @classmethod
    def rentCar(cls):
        cls.getClient()
        # print("asd", client.printClient())

    @staticmethod
    def printMainMenu():
        print("======Menu======")
        print("Get all cars - 1")
        print("Rent a car - 2")
        print("Get all free cars - 3")
        print("Get all rented cars - 4")

    @classmethod
    def run(cls):
        cls.clients.append(Client.from_strings("asd asd 9"))
        while True:
            cls.printMainMenu()
            command = input("Enter command: ")
            if command == "exit":
                break

            switch = {
                '1': cls.printCars,
                '2': cls.rentCar
            }

            switch.get(command, lambda: print("Wrong command"))()
