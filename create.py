import random
import math


def create_random_points(w, h, cell_count):
    return [(
        random.randint(0, w-1), # x
        random.randint(0, h-1), # y
        (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) # color (r, g, b)
        ) for _ in range(cell_count)]


def add_points(image, points):
    w = len(image)
    h = len(image[0])
    point_size = math.ceil(w/200)
    new_image = image.copy()
    for row in range(w):
        for col in range(h):
            for point in points:
                if col < point[0]+point_size and col > point[0]-point_size\
                    and row < point[1]+point_size and row > point[1]-point_size:
                    new_image[row][col] = "0 0 0  "
        
    return new_image


def calculate_euclidean(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
    

def calculate_manhattan(x1, y1, x2, y2):
    return abs(x1-x2)+abs(y1-y2)


def create_voronoi(image, points, distance_type="euclidean", show_points=True):
    w = len(image)
    h = len(image[0])
    new_image = image.copy()
    for row in range(w):
        for col in range(h):
            min_distance = w*h
            min_point = ""
            for point in points:
                distance = 0
                if distance_type == "euclidean":                    
                    distance = calculate_euclidean(col, row, point[0], point[1])
                elif distance_type == "manhattan":
                    distance = calculate_manhattan(col, row, point[0], point[1])
                if distance < min_distance:
                    min_distance = distance
                    min_point = point
            new_image[row][col] = " ".join(map(str, min_point[2])) + "  "
            
    if show_points:
        add_points(new_image, points)
    
    return new_image


def write_ppm(image, filename):
    w = len(image)
    h = len(image[0])
    PPM_HEADER = f"P3\n{h} {w} 255\n"
    ppm_output = PPM_HEADER

    for row in image:
        for col in row:
            ppm_output += str(col)
        ppm_output += "\n"
        
    with open(filename, "wb") as f:
        f.write(ppm_output.encode())