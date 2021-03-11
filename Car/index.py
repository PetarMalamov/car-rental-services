class Car:
    def __init__(self, manufacturer, model, fuelConsumption, regNumber, pricePerHour):
        self.model = model
        self.manufacturer = manufacturer
        self.fuelConsumption = fuelConsumption
        self.regNumber = regNumber
        self.pricePerHour = pricePerHour
        self.pricePerDay = pricePerHour * 24
        self.pricePerWeek = pricePerHour * 168
