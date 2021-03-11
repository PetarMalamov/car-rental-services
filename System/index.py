from CarFactory.index import CarFactory
from Car.index import Car
from Client.index import Client
import json
import re
import uuid


class System:
    cars = []
    clients = []
    transactions = []

    # TODO: make transactions a separate class

    def initialiseCarsData(self, jsonPath):
        with open(jsonPath) as carsJson:
            carsData = json.load(carsJson)
        self.cars = CarFactory.getCarList(carsData['cars'])

    def createClient(self, clientData):
        print(clientData)

    def printCars(self):
        for car in self.cars:
            car.print()

    def printTransactions(self):
        for transaction in self.transactions:
            print(transaction)

    def printNotRentedCars(self, currentlyChoosenCars=[]):
        for car in self.cars:
            if car.getRentedTo() is None and not (
                    any(chosenCar["regNumber"] == car.getRegNumber() for chosenCar in currentlyChoosenCars)):
                car.print()

    def printAllRentedCars(self):
        for car in self.cars:
            if car.getRentedTo() is not None:
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
            print("Choose a car")
            self.printNotRentedCars(carsToRent)
            chosenCar = input("Enter car reg number: ")
            if any(car.regNumber == chosenCar for car in self.cars):
                rentTime = input('Enter time (when entering a number end with h/d/w): ')
                carsToRent.append({"regNumber": chosenCar, "rentTime": self.rentHours(rentTime)})
            else:
                print("No car with that register number found")
                continue

            addMore = input("Add more cars (Yes/No): ")
            if addMore == 'No' or addMore == "no":
                break

        totalPrice = 0
        for carTR in carsToRent:
            choosenCar = next((car for car in self.cars if car.getRegNumber() == carTR['regNumber']), None)
            choosenCar.setRentedTo(currentClient.getEgn())
            totalPrice += choosenCar.getPrice(carTR['rentTime'])

        calculatedPrice = totalPrice * 0.7 if len(carsToRent) >= 3 else totalPrice
        newTransaction = dict(id=uuid.uuid1(), client=currentClient.getEgn(), cars=carsToRent,
                              totalPrice=calculatedPrice)
        self.transactions.append(newTransaction)

    def rentHours(self, time):
        if 'w' in time:
            return int(re.search(r'\d+', time).group()) * 168
        elif 'd' in time:
            return int(re.search(r'\d+', time).group()) * 24
        else:
            return int(re.search(r'\d+', time).group())

    def getTransactionsForClient(self):
        egnFromInput = input("Enter client EGN :")
        currentClient = next((client for client in self.clients if client.getEgn() == egnFromInput), None)

        if currentClient is None:
            print("Client with this egn doesn't exist")
            return

        hasTransactions = any(transaction["client"] == currentClient.getEgn() for transaction in self.transactions)

        if not (hasTransactions):
            print("This client doesn't have transactions")
            return

        for transaction in self.transactions:
            if transaction["client"] == currentClient.getEgn():
                print(transaction)

    def printMainMenu(self):
        print("======Menu======")
        print("Rent a car - 1")
        print("Get All transactions - 2")
        print("Get client transactions - 3")
        print("Get client total due amount - 4")
        print("Get all cars - 5")
        print("Get all free cars - 6")
        print("Get all rented cars - 7")
        print("Exit - 8")

    #    TODO: add search transaction by id

    def run(self):
        self.clients.append(Client.from_strings("asd asd 9"))
        while True:
            self.printMainMenu()
            command = input("Enter command: ")
            if command == "8":
                break

            switch = {
                '1': self.rentCar,
                "2": self.printTransactions,
                "3": self.getTransactionsForClient,
                '5': self.printCars,
                '6': self.printAllRentedCars,
                '7': self.printNotRentedCars
            }

            switch.get(command, lambda: print("Wrong command"))()
