import math
def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height
def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)
radius = 3
height = 7
volume = cylinder_volume(radius, height)
surface_area = cylinder_surface_area(radius, height)

print(f"Volume: {volume:.2f}")
print(f"Surface Area: {surface_area:.2f}")