import math
def get_area(shape):
    shape = shape.lower()
    if shape == "rectangular":
        rectangle_area()
    elif shape == "circular":
        circular_area()
    else:
        print('Enter among circle or rectangle ')

def rectangle_area():
    length = float(input("Enter the Length "))
    width = float(input("Enter the Width "))
    area = length * width
    print("Area of the rectangle is ",area)

def circular_area():
    radius = float(input("Enter the radius "))
    area = math.pi * (math.pow(radius,2))
    print("The area of the circle is {:.2f}".format(area))


def main():
    shape_type = input("Enter the shape type ")
    get_area(shape_type)

main()
