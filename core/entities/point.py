class Point():
    """Cellular Point into Table(Vecindario) """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def toString(self):
        return 'Point(x={0}, y={0})'.format(self.x, self.y)

    def isANeighbour(self, point):
        return ((point.x == self.x + 1) or (point.x == self.x) or (point.x < self.x - 1)) and ((point.y == self.y + 1 ) or (point.y == self.y) or (point.y == self.y - 1 ))
       
 

        


      


