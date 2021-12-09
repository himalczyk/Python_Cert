from math import hypot, sqrt
from models import Point2D, Point3D

class Point2DController:
    def calculate_distance(self, p1, p2):
        return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    def compare_0_0(self, p1, p2):
        return hypot(p1.x, p1.y) > hypot(p2.x, p2.y)
class Point3DController:
    def __init__(self):
        self.__points3d = []
    def calculate_distance(self, p1: Point3D, p2: Point3D):
        return sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2)
    def compare_0_0(self, p1: Point3D, p2: Point3D):
        return hypot(p1.x, p1.y, p1.z) > hypot(p2.x, p2.y, p2.z)
    def add_point(self, p):
        self.__points3d.append(p)
    def get_points(self):
        for p in self.__points3d:
            print(p)
        
p2d = Point2DController()
print("[1,1][2,2] dist= ",  p2d.calculate_distance(Point2D(1, 1), Point2D(2, 2)))
print("[1,1][2,2] compare dist to 0= ",  p2d.compare_0_0(Point2D(1, 1), Point2D(2, 2)))
p3d = Point3DController()
print("[1,1,1][2,2,2] dist= ",  p3d.calculate_distance(Point3D(1, 1,1), Point3D(2, 2, 2)))
print("[1,1,2][2,2,2] compare dist to 0= ",  p3d.compare_0_0(Point3D(1, 1, 1), Point3D(2, 2, 2)))
p1 = Point3D(1, 2, 3)
p2 = Point3D(3, 2, 3)
p3d.add_point(p1)
p3d.add_point(p2)
p3d.get_points()