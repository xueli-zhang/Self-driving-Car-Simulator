#This file contains helper functions that will be used in neural networks
def loading_training_data(path):
    training_data = []

    f = open(path, "r")

    lines = f.read()

    for line in lines:
        print(line)
        training_data.append(line)
        
    return training_data

def loading_maps_date(path):
    
    maps = []

    f = open(path, "r")

    lines = f.read()

    for line in lines:
        print(line)
        maps.append(line)
    

    return maps