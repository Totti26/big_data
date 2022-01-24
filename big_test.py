import csv

stations = []

class info():
    def __init__(self, name):
        self.name = name
        self.first = True
        
    def cleanData(self, max, min):
        if max > 120 or min < -80:
            return False
        else:
            return True

    def findMaxMin(self, max, min):
        if self.first:
            self.maxTemp = max
            self.minTemo = min
            self.first = False

        if max > self.maxTemp:
            self.maxTemp = max
        if min < self.minTemp:
            self.minTemp = min
            

