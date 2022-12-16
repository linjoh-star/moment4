import math

def circle_area(radius):
  return math.pi * radius**2

def circle_circumference(radius):
  return 2 * math.pi * radius

radius = float(input("Ange cirkelns radie: "))

area = circle_area(radius)
circumference = circle_circumference(radius)

print(f"Area: {area}")
print(f"Omkrets: {circumference}")