class File_obj:
    def __init__(self, x,y,height,width,image = ""):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.image = image
    def __str__(self):
        return "{self.x}, {self.y}, {self.height}, {self.width}, {self.image}"