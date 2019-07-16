#This class is to construct a neural_networks for Praking simulator

class Parking_simulator:
    
    def __init__(self, map):
        self.map = map
        self.speed = 0
        self.angle = 0
        self.acc = 0

        