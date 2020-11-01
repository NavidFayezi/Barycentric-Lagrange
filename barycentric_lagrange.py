

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class BarycentricLagrange:

    # initialize the class with data points
    def __init__(self, data_points):
        self.data_points = data_points
        self.weights = []

    # calculate the weight of data_points[point_index]
    def calculate_weight(self, point_index):
        result = 1
        for i in range(len(self.data_points)):
            if point_index != i :
                result *= self.data_points[point_index].x - self.data_points[i].x
        self.weights.insert(point_index, 1/result)

    def interpolation(self, x):
        numerator = 0
        denominator = 0
        for i in range(len(self.data_points)):
            temp = self.weights[i] / (x-self.data_points[i].x)
            denominator += temp
            numerator += temp * self.data_points[i].y
        return numerator/denominator

    # add a single point to data points
    def add_point(self, new_point):
        for i in range(len(self.data_points)):    # check to see if the x attribute of the new point already exists.
            if new_point.x == self.data_points[i].x:    # if so, only update the y attribute
                self.data_points[i].y = new_point.y
                return
        # update weights
        for i in range(len(self.data_points)):
            self.weights[i] *= 1/(self.data_points[i].x - new_point.x)
        self.data_points.append(new_point)
        # calculate the weight of the new point
        self.calculate_weight(len(self.data_points)-1)


if __name__ == "__main__":
    point1 = Point(2, 4)
    point2 = Point(3, 9)
    point3 = Point(1, 1)
    dp = [point1, point2]
    bl = BarycentricLagrange(dp)
    for i in range(len(dp)):
        bl.calculate_weight(i)
    print(bl.interpolation(5))
    bl.add_point(point3)
    print(bl.interpolation(5))