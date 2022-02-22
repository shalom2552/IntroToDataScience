class Point:
    def __init__(self, name, coordinates, label):
        self.name = name
        self.coordinates = []
        self.set_coordinates(coordinates)
        self.label = label

    def distance_to(self, coordinates, norm=2):
        if not self.coordinates:
            print('Point', self.name, 'not initiated. Please provide coordinates in init or call set_coordinates')
            return 0
        return sum([abs(my-his)**norm for my, his in zip(self.coordinates, coordinates)])**(1/norm)

    def set_coordinates(self, coordinates):
        self.coordinates = [float(x) for x in coordinates]
