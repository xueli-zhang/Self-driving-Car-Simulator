#This file contains helper functions that will be used in neural networks
def loading_training_data(path):
    training_data = []

    f = open(path, "r")

    lines = f.read()

    for line in lines:
        print(line)

    

    return training_data