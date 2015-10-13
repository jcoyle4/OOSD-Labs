from math import pi, acos, sin, cos

#   Global constant for the radius of the Earth
r_earth = float(6371)


def dist(lat_1, lat_2, long_1, long_2):
    #   A function to calculate the distance between two points
    #   Need to convert latitudes to angular distance from the North Pole
    if lat_1 > 0:
        lat_1 = 90 - lat_1
    else:
        lat_1 = 90 + abs(lat_1)

    if lat_2 > 0:
        lat_2 = 90 - lat_2
    else:
        lat_2 = 90 + abs(lat_2)

    #   Convert degrees to radians
    lat_1 = deg_to_rad(lat_1)
    long_1 = deg_to_rad(long_1)
    lat_2 = deg_to_rad(lat_2)
    long_2 = deg_to_rad(long_2)

    #   Return the distance using the given formula
    return acos((sin(lat_1) * sin(lat_2) * cos((long_1 - long_2))) + (cos(lat_1) * cos(lat_2))) * r_earth


def deg_to_rad(angle):
    #   A function to convert degree to radians
    return angle * ((2 * pi) / 360)


def main():

    #   Manually input the coordinates
    latitude_1 = float(input("Enter latitude of location 1: "))
    longitude_1 = float(input("Enter longitude of location 1: "))
    latitude_2 = float(input("Enter latitude of location 2: "))
    longitude_2 = float(input("Enter longitude of location 2: "))

    #   Send the coords to the 'distance' function
    distance = dist(latitude_1, latitude_2, longitude_1, longitude_2)

    print("The distance between your locations is", int(distance))

main()