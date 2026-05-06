# cone_program.py

import threedfigures

def cone_program():
    radius = float(input("Enter the radius of the cone: "))
    height = float(input("Enter the height of the cone: "))
    slant_height = float(input("Enter the slant height of the cone: "))
    
    volume = threedfigures.cone_volume(radius, height)
    curved_surface_area = threedfigures.cone_curved_surface_area(radius, slant_height)
    total_surface_area = threedfigures.cone_total_surface_area(radius, slant_height)
    
    print(f"Volume of the Cone: {volume:.2f} cubic units")
    print(f"Curved Surface Area of the Cone: {curved_surface_area:.2f} square units")
    print(f"Total Surface Area of the Cone: {total_surface_area:.2f} square units")

if __name__ == "__main__":
    cone_program()