import random
import math

def generate_random_points(n):
    points = [(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(n)]
    return points
def calculate_distance(point):
    return math.sqrt(point[0]**2 + point[1]**2)
points = generate_random_points(5)
distances = {point: calculate_distance(point) for point in points}

print("Список точек:", points)
print("Словарь точек и их расстояний до начала координат:", distances)
