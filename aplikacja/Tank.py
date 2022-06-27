class Tank:
    def __init__(self,name, range, speed, caliber, weight, year, country):
        self.name = name
        self.range = range
        self.speed = speed
        self.caliber = caliber
        self.weight = weight
        self.year = year
        self.country = country
    def print_info(self):
        print('name: ' + self.name + '  range: ' + self.range + '  max speed: ' + self.speed +
              '  caliber: ' + self.caliber + '  weight ' + self.weight + '  year ' +
              self.year + '  country ' + self.country)
    def return_weight(self):
            return self.weight

