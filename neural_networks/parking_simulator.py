#This class is to construct some random maps and setups for testing AV
import random
import pedestrians


class Parking_simulator:
    
    def __init__(self, map=[]):
        self.map = map

    #This function is to generate pedestrians with random number, random position and random states.
    def generate_pedes(self, min = 0, max = 10):

        numOfPed = random.randint(min, max)

        peds = []

        print("generating "+str(numOfPed)+" pedestrians. ")

        for _ in range(numOfPed):
            peds.append(pedestrians.Pedestrians(random.randint(0,2)))

        
        print("there are "+str(len(peds))+" pedestrians generated. ")


        return

    


def main():
    parkSim = Parking_simulator() 

    parkSim.generate_pedes(10, 20)

if __name__ == "__main__":
    main()