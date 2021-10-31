import math


def calculate_distance(point1, point2):
    return math.sqrt(((int(point1[0]) - int(point2[0])) ** 2) + ((int(point1[1]) - int(point2[1])) ** 2))


point1_coordinate = input("enter first coordinate of line1: ")
point1_coordinate = point1_coordinate.split(",")

point2_coordinate = input("enter second coordinate of line1 : ")
point2_coordinate = point2_coordinate.split(",")

length_of_line1 = calculate_distance(point1_coordinate, point2_coordinate)

point1_coordinate = input("enter first coordinate of line2: ")
point1_coordinate = point1_coordinate.split(",")

point2_coordinate = input("enter second coordinate of line2 : ")
point2_coordinate = point2_coordinate.split(",")

length_of_line2 = calculate_distance(point1_coordinate, point2_coordinate)

if length_of_line1==length_of_line2:
    print("both lines are equal")
elif length_of_line1>length_of_line2:
    print("Line1 is greater than line 2")
else:
    print("Line2 is greater than Line1")


