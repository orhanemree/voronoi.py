import sys
from create import *
from convert import *

if __name__ == "__main__":
    WIDTH = 500
    HEIGHT = 250
    CELL_COUNT = 50

    image = [[0] * WIDTH for _ in range(HEIGHT)]
    points = create_random_points(WIDTH, HEIGHT, CELL_COUNT)

    image_euclidean = create_voronoi(image, points, distance_type="euclidean", show_points=True)
    write_ppm(image, "out/euclidean.ppm")
    ppm2png("out/euclidean.ppm")
    
    image_manhattan = create_voronoi(image, points, distance_type="manhattan", show_points=True)
    write_ppm(image, "out/manhattan.ppm")
    ppm2png("out/manhattan.ppm")
    