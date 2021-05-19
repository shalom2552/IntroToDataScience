class Point:
    def __init__(self, name, coordinates=None):
        self.name = name
        self.coordinates = []
        if coordinates:
            self.set_coordinates(coordinates)

    def distance_to(self, coordinates):
        if not self.coordinates:
            print('Point', self.name, 'not initiated. Please provide coordinates in init or call set_coordinates')
            return 0
        return sum([abs(my-his) for my, his in zip(self.coordinates, coordinates)])

    def set_coordinates(self, coordinates):
        self.coordinates = [float(x) for x in coordinates]
