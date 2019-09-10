import objects.static_object as static_object
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
    new_object = None

    f = open(path, "r")

    lines = f.read()

    for line in lines:
        if line == "t":
            new_object = static_object("image/path","tree", 10, 15, 30)
        print(line)
        maps.append(new_object)
    

    return maps

def main():
    loading_maps_date("./maps/map01.txt")

if __name__ == "__main__":
    main()