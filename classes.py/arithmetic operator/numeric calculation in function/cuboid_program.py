# cuboid_program.py

import threedfigures

def cuboid_program():
    length = float(input("Enter the length of the cuboid: "))
    width = float(input("Enter the width of the cuboid: "))
    height = float(input("Enter the height of the cuboid: "))
    
    volume = threedfigures.cuboid_volume(length, width, height)
    surface_area = threedfigures.cuboid_surface_area(length, width, height)
    
    print(f"Volume of the Cuboid: {volume:.2f} cubic units")
    print(f"Surface Area of the Cuboid: {surface_area:.2f} square units")

if __name__ == "__main__":
    cuboid_program()