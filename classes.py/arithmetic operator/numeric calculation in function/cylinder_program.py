# cylinder_program.py

import threedfigures

def cylinder_program():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height of the cylinder: "))
    
    volume = threedfigures.cylinder_volume(radius, height)
    curved_surface_area = threedfigures.cylinder_curved_surface_area(radius, height)
    total_surface_area = threedfigures.cylinder_total_surface_area(radius, height)
    
    print(f"Volume of the Cylinder: {volume:.2f} cubic units")
    print(f"Curved Surface Area of the Cylinder: {curved_surface_area:.2f} square units")
    print(f"Total Surface Area of the Cylinder: {total_surface_area:.2f} square units")

if __name__ == "__main__":
    cylinder_program()