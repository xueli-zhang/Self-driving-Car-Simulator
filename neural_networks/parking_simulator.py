#This class is to construct some random maps and setups for testing AV

class Parking_simulator:
    
    def __init__(self, map):
        self.map = map

    #This function is to generate pedestrians with random number, random position and random states.
    def generate_pedes(self):
        numOfPed = 0

