import math

r1 = 123
r2 = 567
r3 = 10000000

# a1 = 3.14159 * r1 * r1
# a2 = 3.14159 * r2 * r2
# a3 = 3.14159 * r3 * r3

# print(a1, a2, a3)


def area_of_circle(x):
    """print the area of a circle, given the radius value"""
    # area = 3.14159535 * x * x
    area = math.pi * x * x
    print(area)


area_of_circle(r1)  # call the function
area_of_circle(r2)
area_of_circle(r3)


# def area_of_circles(radius):
#     """calculate areas of multiple circles, given a list of radius values"""
#     for r in radius:
#         area_of_circle(r)


# rs = [r1, r2, r3]
# area_of_circles(rs)
