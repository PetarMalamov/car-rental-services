class Car:
    def __init__(self, manufacturer, model, fuelConsumption, regNumber, pricePerHour, rentedTo):
        self.model = model
        self.manufacturer = manufacturer
        self.fuelConsumption = fuelConsumption
        self.regNumber = regNumber
        self.pricePerHour = pricePerHour
        self.pricePerDay = pricePerHour * 24
        self.pricePerWeek = pricePerHour * 168
        self.rentedTo = rentedTo
        # self.rentedFor = rentedFor
        # in hours

    def setRentedTo(self, egn):
        self.rentedTo = egn

    def getRentedTo(self):
        return self.rentedTo

    def getRegNumber(self):
        return self.regNumber

    def getPrice(self,hours):
        return self.pricePerHour * hours

    def print(self):
        isRented = 'rented' if self.rentedTo is not None else 'not rented'
        print(
            f'{self.manufacturer} {self.model} {self.regNumber} {self.fuelConsumption} {self.pricePerDay} - {isRented}')
