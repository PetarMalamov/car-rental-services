from System.index import System

if __name__ == '__main__':
    carSystem = System()
    carSystem.initialiseCarsData('carsList.json')
    carSystem.run()
