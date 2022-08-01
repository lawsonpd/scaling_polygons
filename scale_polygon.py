import random
import math
import itertools
import sys
import os

xlim, ylim = 500, 500

num_coords = lambda: random.randint(3, 10)

gen_coords = lambda xlim, ylim: (random.randint(-xlim, xlim), random.randint(-ylim, ylim))

# coords = [gen_coords(xlim, ylim) for _ in num_coords]

def euc_dist(p1, p2):
    return math.sqrt((p2[1] - p1[1]) ** 2 + (p2[0] - p1[0]) ** 2)

# def scale_poly(coords, scale_factor):
#     new_coords = []
#     for p1, p2 in itertools.combinations(coords, 2):
#         dist = euc_dist(p1, p2)
#         dist_to_move_current_point = (scale_factor * dist_to_next_point / 2) - \
#                                     (dist_to_next_point / 2)

# def scale_side_lengths(verts, scale_factor):
#     return [euc_dist(p1, p2) * scale_factor for p1, p2 in itertools.combinations(verts, 2)]

def scale_vector(vector, scale_factor):
    x, y = vector
    return scale_factor * x, scale_factor * y

def scale_polygon(vectors, scale_factor):
    return [scale_vector(v, scale_factor) for v in vectors]

def polygon_perimeter(coords):
    return sum([euc_dist(v1, v2) for v1, v2 in itertools.combinations(coords, 2)])

if len(sys.argv) != 2:
    raise ValueError("Please provide only the scaling factor (int) argument")
scaling_factor = int(sys.argv[1])
pgon = [gen_coords(xlim, ylim) for _ in range(num_coords())]
print(f'Initial coordinates: {pgon}\n')
pgon_scaled = scale_polygon(pgon, scaling_factor)
print(f'Coordinates scaled by a factor of {scaling_factor}: {pgon_scaled}\n')
init_perimeter = polygon_perimeter(pgon)
scaled_perimeter = polygon_perimeter(pgon_scaled)
print(f'Perimeter of original polygon: {init_perimeter}\n')
print(f'Perimeter of scaled polygon: {scaled_perimeter}\n')
print(f'Perimeters ratio: {scaled_perimeter / init_perimeter}')

