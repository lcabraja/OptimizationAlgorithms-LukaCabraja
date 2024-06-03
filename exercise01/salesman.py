import random
import itertools

length = 4

def generate_coordinates(n):
    coordinates = []
    for _ in range(n):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        coordinates.append([x, y])
    return coordinates

# a = [x1, y1], b = [x2, y2]
def calculate_distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

def salesman(points):
    nums = range(len(points))
    permutations = list(itertools.permutations(nums))
    shortest = None
    order = None

    for p in permutations:
        distance = 0
        for i in range(len(p)):
            if i == len(p) - 1:
                distance += calculate_distance(points[p[i]], points[p[0]])
            else:
                distance += calculate_distance(points[p[i]], points[p[i + 1]])
        if shortest is None or distance < shortest:
            shortest = distance
            order = p

    return order
    

points = generate_coordinates(length)
print(f"Generated {length} points: {points}")

order = salesman(points)
print("Best order for salesman: ", order)