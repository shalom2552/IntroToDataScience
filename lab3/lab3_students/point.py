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
        return sum([(my-his)**2 for my, his in zip(self.coordinates, coordinates)])**0.5

    def set_coordinates(self, coordinates):
        self.coordinates = [float(x) for x in coordinates]
