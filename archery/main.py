import math
from typing import List, Tuple


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point(x={self.x},y={self.y})"

    def __repr__(self) -> str:
        return self.__str__()

    def distance_to_origin(self) -> float:
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __lt__(self, other):
        return self.distance_to_origin() < other.distance_to_origin()


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    def __str__(self) -> str:
        return f"Line(p1={self.p1},p2={self.p2}"

    def __repr__(self) -> str:
        return self.__str__()


class Circle:
    def __init__(
        self, radius: float, x_origin: float = 0.0, y_origin: float = 0.0
    ) -> None:
        self.radius = radius
        self.x_origin = x_origin
        self.y_origin = y_origin

    def __lt__(self, other_circle) -> bool:
        return self.radius < other_circle.radius

    def contains_point(self, point: Point) -> bool:
        delta_x = point.x - self.x_origin
        delta_y = point.y - self.y_origin
        return delta_x * delta_x + delta_y * delta_y < self.radius * self.radius

    def __str__(self) -> str:
        return f"Circle(radius={self.radius},x_origin={self.x_origin},y_origin={self.y_origin})"

    def __repr__(self) -> str:
        return self.__str__()


def read_input() -> Tuple[List[Circle], List[Line]]:
    circles = []
    lines = []
    input_lines = []

    while True:
        try:
            input_lines.append(input())
        except EOFError:
            break

    for i in range(len(input_lines)):
        input_lines[i] = input_lines[i].replace("\n", "")

    radii = input_lines[1].split(" ")
    for radius in radii:
        circles.append(Circle(float(radius)))

    for line in input_lines[3:]:
        line = line.split(" ")
        p1 = Point(x=float(line[0]), y=float(line[1]))
        p2 = Point(x=float(line[2]), y=float(line[3]))
        lines.append(Line(p1=p1, p2=p2))

    return circles, lines


def count_Qs(circles: List[Circle], lines: List[Line]) -> int:
    result = 0
    for line in lines:
        for circle in circles:
            contains_at_least_one_point = circle.contains_point(
                line.p1
            ) ^ circle.contains_point(line.p2)
            if contains_at_least_one_point:
                result += 1

    return result


def count_Qs_fast(circles: List[Circle], lines: List[Line]) -> int:
    result = 0
    circles.sort()

    for line in lines:
        lower_point, higher_point = sorted([line.p1, line.p2])

        lo, hi = 0, len(circles) - 1
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            current_circle = circles[mid]
            if current_circle.contains_point(lower_point):
                hi = mid
            else:
                lo = mid + 1

        innermost_idx = lo

        outtermost_idx = -1
        lo, hi = 0, len(circles) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            current_circle = circles[mid]
            if current_circle.contains_point(higher_point):
                hi = mid - 1
            else:
                outtermost_idx = mid
                lo = mid + 1

        # all circles which are closer to the origin than both p1 and p2 have been intersected twice and thus should not be added
        if (
            circles[innermost_idx].radius >= line.p1.distance_to_origin()
            or circles[outtermost_idx].radius >= line.p2.distance_to_origin()
        ):
            result += outtermost_idx - innermost_idx + 1

    return result


circles, lines = read_input()
print(count_Qs_fast(circles, lines))
