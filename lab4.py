import math
import data

# Write your functions for each part in the space below.

# Part 1
def first_element(input: list[list[int]]) -> list[int]:
    test_list = [real_list for real_list in input if len(real_list) > 0]
    final_list = [real_list[0] for real_list in test_list]
    return final_list

# Part 2
def x_coordinates(points: list[data.Point]):
    return [point.x for point in points]
# Part 3
def in_positive_quadrant(points: list[data.Point]) -> list[data.Point]:
    return [point for point in points if point.x > 0 and point.y > 0]

# Part 4
def distance(p1: data.Point, p2: data.Point) -> float:
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

# Part 5
def manhattan_distance(p1: data.Point, p2: data.Point) -> float:
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)

# Part 6
def distance_all(points: list[data.Point]) -> list[float]:
    origin = data.Point(0, 0)
    return [distance(point, origin) for point in points]

