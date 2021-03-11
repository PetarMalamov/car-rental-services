from CarFactory.index import CarFactory
from Car.index import Car
from Client.index import Client
import json


class System:
    cars = []
    clients = []

    def initialiseCarsData(self, jsonPath):
        with open(jsonPath) as carsJson:
            carsData = json.load(carsJson)
        self.cars = CarFactory.getCarList(carsData['cars'])

    def createClient(self, clientData):
        print(clientData)

    def printCars(self):
        print("self.cars", self.cars)
        for car in self.cars:
            car.print()

    # def printNotRentedCars(self):
    #     for car in self.cars:

    def getClient(self):
        egnFromInput = input("Enter client egn: ")
        currentClient = None
        for client in self.clients:
            if client.getEgn() == egnFromInput:
                print("here")
                currentClient = client
                break

        if currentClient is None:
            print("No client Found")
            print("Please add client to the system")
            newClient = input("Enter person first name, last name, egn: ")
            currentClient = Client.from_strings(newClient)
            self.clients.append(currentClient)

        currentClient.print()
        return currentClient

    def rentCar(self):
        self.getClient()
        # print("asd", client.printClient())

    @staticmethod
    def printMainMenu():
        print("======Menu======")
        print("Get all cars - 1")
        print("Rent a car - 2")
        print("Get all free cars - 3")
        print("Get all rented cars - 4")
        print("Exit - 5")

    def run(self):
        self.clients.append(Client.from_strings("asd asd 9"))
        while True:
            self.printMainMenu()
            command = input("Enter command: ")
            if command == "5":
                break

            switch = {
                '1': self.printCars,
                '2': self.rentCar
            }

            switch.get(command, lambda: print("Wrong command"))()
