# threedfigures.py

import math

# Cube
def cube_volume(side):
    return side**3

def cube_surface_area(side):
    return 6 * side**2

# Cuboid
def cuboid_volume(length, width, height):
    return length * width * height

def cuboid_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

# Cylinder
def cylinder_volume(radius, height):
    return math.pi * radius**2 * height

def cylinder_curved_surface_area(radius, height):
    return 2 * math.pi * radius * height

def cylinder_total_surface_area(radius, height):
    return 2 * math.pi * radius * (height + radius)

# Cone
def cone_volume(radius, height):
    return (1/3) * math.pi * radius**2 * height

def cone_curved_surface_area(radius, slant_height):
    return math.pi * radius * slant_height

def cone_total_surface_area(radius, slant_height):
    return math.pi * radius * (slant_height + radius)

# Sphere
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def sphere_surface_area(radius):
    return 4 * math.pi * radius**2

# Hemisphere
def hemisphere_volume(radius):
    return (2/3) * math.pi * radius**3

def hemisphere_surface_area(radius):
    return 3 * math.pi * radius**2