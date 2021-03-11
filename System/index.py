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
        for car in self.cars:
            car.print()

    def printNotRentedCars(self, currentlyChoosenCars):
        print(currentlyChoosenCars)
        for car in self.cars:
            if car.getRentedTo() is None and not (
                    any(chosenCar["regNumber"] == car.getRegNumber() for chosenCar in currentlyChoosenCars)):
                car.print()

    def getClient(self):
        egnFromInput = input("Enter client egn: ")
        currentClient = next((client for client in self.clients if client.getEgn() == egnFromInput), None)

        if currentClient is None:
            print("No client Found")
            print("Please add client to the system")
            newClient = input("Enter person first name, last name, egn: ")
            currentClient = Client.from_strings(newClient)
            self.clients.append(currentClient)

        return currentClient

    def rentCar(self):
        currentClient = self.getClient()
        carsToRent = []

        while True:
            print("Choose car")
            self.printNotRentedCars(carsToRent)
            chosenCar = input("Enter car reg number: ")
            if any(car.regNumber == chosenCar for car in self.cars):
                rentTime = input('Enter time (when entering a number end with h/d/w): ')
                carsToRent.append({"regNumber": chosenCar, "rentTime": rentTime})
            else:
                print("No car with that register number found")
                continue

            addMore = input("Add more cars (Yes/No): ")
            if addMore == 'No' or addMore == "no":
                break

        print(carsToRent)
        for cr in carsToRent:
            choosenCar = next((car for car in self.cars if car.getRegNumber() == cr['regNumber']), None)
            choosenCar.setRentedTo(currentClient.getEgn())

        # print("asd", client.printClient())

    def printMainMenu(self):
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
