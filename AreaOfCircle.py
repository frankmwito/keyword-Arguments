# return the area of a circle accepting radius as a keyword argument
import math

def area_circle(radius):
    area = math.pi * math.pow(radius, 2)
    return area

result = area_circle(radius=22)

print("The area of circle is:", round(result, 2))