import math


r1 = 20.16
r2 = 9.13
r3 = 11.55

# a1 = 3.14 * r1 * r1
# a2 = 3.14 * r2 * r2
# a3 = 3.14 * r3 * r3

# print(a1, a2, a3)


def area_of_circle(r):
    """print the area of a circle given the radius value"""
    area = math.pi * r * r
    print(area)


area_of_circle(r1)
area_of_circle(r2)
area_of_circle(r3)


# TODO: 3.5//1 ?