class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def create_point_object(n):
    x, y = map(int, n.split())
    return Point(x, y)


def ex1(points):
    inside_counter = 0
    for point in points:
        if pow(point.x - 200, 2) + pow(point.y - 200, 2) == 40000:
            print(point)
            continue
        if pow(point.x - 200, 2) + pow(point.y - 200, 2) < 40000:
            inside_counter += 1
    print(inside_counter)


def count_pi(points):
    circle_points_counter = 0
    square_point_counter = 0
    for point in points:
        if pow(point.x - 200, 2) + pow(point.y - 200, 2) <= 40000:
            circle_points_counter += 1
            square_point_counter += 1
            continue
        if 0 <= point.x <= 400 and 0 <= point.y <= 400:
            square_point_counter += 1
    return round(circle_points_counter/square_point_counter * 4, 4)


def ex2(points):
    print(count_pi(points[:1000]))
    print(count_pi(points[:5000]))
    print(count_pi(points))


def main():
    with open("punkty.txt", "r") as file:
        points = list(map(create_point_object, file.readlines()))
    ex1(points)
    ex2(points)


if __name__ == "__main__":
    main()
