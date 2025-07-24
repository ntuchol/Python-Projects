class Rectangle:
    def __init__(self, bottom_left, top_right):
        
        self.x1, self.y1 = bottom_left
        self.x2, self.y2 = top_right

    def area(self):
        
        return (self.x2 - self.x1) * (self.y2 - self.y1)

    def perimeter(self):
        return 2 * ((self.x2 - self.x1) + (self.y2 - self.y1))

    def contains_point(self, point):
        
        x, y = point
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2

    def intersect(self, other):
        
        return not (self.x2 < other.x1 or self.x1 > other.x2 or
                    self.y2 < other.y1 or self.y1 > other.y2)



rect1 = Rectangle((1, 1), (4, 4))
rect2 = Rectangle((3, 3), (6, 6))
point = (2, 2)

print("Area of rect1:", rect1.area())
print("Perimeter of rect1:", rect1.perimeter())
print("Does rect1 contain the point?", rect1.contains_point(point))
print("Do rect1 and rect2 intersect?", rect1.intersect(rect2))
