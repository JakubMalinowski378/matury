from math import sqrt, pow


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x},y:{self.y})"


def create_point(n):
    n = n.split()
    return Point(int(n[0]), int(n[1]))


def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def ex1(points):
    counter = 0
    for point in points:
        if is_prime(point.x) and is_prime(point.y):
            counter += 1
    print(counter)


def ex2(points):
    counter = 0
    for point in points:
        if set(str(point.x)) == set(str(point.y)):
            counter += 1
    print(counter)


def ex3(points):
    max_distance = 0
    point1 = Point(0, 0)
    point2 = Point(0, 0)
    for i in range(len(points)):
        for j in range(i, len(points)):
            pointA = points[i]
            pointB = points[j]
            distance = pow(pointA.x - pointB.x, 2) + pow(pointA.y - pointB.y, 2)
            if distance > max_distance:
                max_distance = distance
                point1 = pointA
                point2 = pointB
    max_distance = round(sqrt(max_distance))
    print(f"Distance = {max_distance}\nA({point1.x}, {point1.y})\nB({point2.x}, {point2.y})")


def ex4(points):
    inside, outside, onside = 0, 0, 0
    for point in points:
        # inside
        if abs(point.x) < 5000 and abs(point.y) < 5000:
            inside += 1
            continue
        # outside
        if abs(point.x) > 5000 or abs(point.y) > 5000:
            outside += 1
            continue
        onside += 1
    print(f"inside: {inside}\noutside: {outside}\nonside: {onside}")


def main():
    with open("punkty.txt", "r") as file:
        points = list(map(create_point, file.readlines()))
    # print(points)
    ex1(points)
    ex2(points)
    ex3(points)
    ex4(points)


if __name__ == "__main__":
    main()
