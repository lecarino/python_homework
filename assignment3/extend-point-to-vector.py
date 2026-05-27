import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __eq__(self, alt_point):
        if self.x == alt_point.x and self.y == alt_point.y:
            return True
        else:
            return False
           

    def __str__(self):
        return f"Point: ({self.x}, {self.y})"

    def euclidian_distance(self, alt_point):
        #Find the difference, square, add, sqrt
        return (math.sqrt((alt_point.x - self.x)**2 + (alt_point.y - self.y)**2))
        

class Vector(Point):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __str__(self):
        return f"Vector Point: ({self.x}, {self.y})"
    
    def __add__(self, alt_point):
        new_x = self.x + alt_point.x
        new_y = self.y + alt_point.y
        return Vector(new_x, new_y)

    

point1 = Point(6,7)
point2 = Point(1,2)
point3 = Point(6,7)
vector = Vector(9,7)

#CASE1: NOT EQUAL
print(point1 == (point2))

#CASE2: EQUAL
print(point1 == (point3))

#CASE3: Point string rep:
print(point1)

#CASE4: Vector string rep:
print(vector)

#CASE5: euclidian distance b/w points
print(point1.euclidian_distance(point2))

#CASE6: euclidian distance b/w point and vector
print(point1.euclidian_distance(vector))

#CASE7: add vector
print(vector + point3)
