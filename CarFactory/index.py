from Car.index import Car


class CarFactory:

    @staticmethod
    def getCarList(carList):
        # print("here",carList)
        cars = []
        for car in carList:
            # print("car",car)
            carObject = Car(car['manufacturer'], car['model'], car['fuelConsumption'], car['regNumber'],
                            car['pricePerHour'])
            cars.append(carObject)
        return cars
