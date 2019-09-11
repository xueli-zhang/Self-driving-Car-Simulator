from objects.static_object import Static_object
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
            new_object = Static_object("image/path","tree", 10, 15, 30)
        elif line == "r":
            new_object = Static_object("image/path","road", 0, 50, 30)
        elif line == "b":
            new_object = Static_object("image/path","building", 100, 30, 10)
        
        maps.append(new_object)
    print(maps)
    

    return maps

def main():
    loading_maps_date("./maps/map01.txt")

if __name__ == "__main__":
    main()