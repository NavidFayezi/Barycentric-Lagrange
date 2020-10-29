


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class BarycentricLagrange:

    def __init__(self, data_points):
        self.data_points = data_points
        self.weights = []

    def calculate_weight(self, point_index):
        result = 1
        for i in range(len(self.data_points)):
            if point_index != i :
                result *= self.data_points[point_index].x - self.data_points[i].x
        self.weights.insert(point_index, 1/result)





if __name__ == "__main__":
    point1 = Point(4, 21.5)
    point2 = Point(3.4, 117.10)
    point3 = Point(5.2, 531.5)
    dp = [point1, point2, point3]
    bl = BarycentricLagrange(dp)
    for i in range(len(dp)):
        bl.calculate_weight(i)
    print(bl.weights)