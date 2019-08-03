#This class is for creating pedestrians AI objects.
import parking_helper

pede_id = 0000000
training_data_path = "./ped/park_sim/ped_training.txt"

class Pedestrians:

    #there are 2 behavor types: normal behavior 0 or abnormal behavior 1(not expecting situations)
    def __init__(self, behav_type = 0):
        self.id = pede_id + 1
        self.behav_type = behav_type

    def pede_ai(self):
        if self.behav_type == 0:
            #generate ai from neural network pedetrains normal
            pass
        elif self.behav_type == 1:
            #generate ai from neural network pedtrains abnormal
            pass
        else:
            print ("Error: Unexpected behavior type not 0 or 1")

    #this function is to load training data for pedestrains neural network to train pedestrains with 0 normal behavior data or 1 abnormal behavior data
    #no return
    def loading_pede_train_data(self, type=0):
        parking_helper.loading_training_data(training_data_path)

    #this function is to control pedestrains act normally. Define a set of normal behaviors: 1. avoding car when it detected...
    #return a basic behavior at a call: move_forward, turn #degrees, move_backward...
    #using the same neural networks of abnormal_pedetrains_ai, but just trained with different behavior set
    def normal_pedetrains_ai(self):
        pass

    #this function is to control pedestrians act abnomarlly. Define a set of abnormal behaviors: 1. move to the front of the car to stop car moving...
    #return a basic behavior at a call: move_forward, turn #degrees, move_backward...
    #using the same neural networks of normal_pedetrains_ai, but just trained with different behavior set
    def abnormal_pedetrains_ai(self):
        pass


    
