#This class is for construct static objects that correspoding to the maps.

class Static_Object:

    def __init__(self, image_path, object_name, height, width, angle):

        self.image_path = image_path #the image of the object, width can be used for computer vision
        self.object_name = object_name #corresponding to r, t, b...in HD maps
        self.height = height #object height
        self.width = width #object width
        self.angle = angle #corresponding to the angle the object facing the road. 

