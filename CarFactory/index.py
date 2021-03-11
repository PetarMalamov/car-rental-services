from Car.index import Car


class CarFactory:

    @staticmethod
    def getCarList(carList):
        cars = []
        for car in carList:
            carObject = Car(car['manufacturer'], car['model'], car['fuelConsumption'], car['regNumber'],
                            car['pricePerHour'], car['rentedTo'])
            cars.append(carObject)
        return cars
