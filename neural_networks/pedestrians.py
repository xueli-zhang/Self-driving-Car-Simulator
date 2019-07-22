#This class is for creating pedestrians AI objects.

pede_id = 0000000

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

    
