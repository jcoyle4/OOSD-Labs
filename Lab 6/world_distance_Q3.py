from math import pi, acos, sin, cos

r_earth = 6371


def dist(lat_1, lat_2, long_1, long_2):

    if lat_1 > 0:
        lat_1 = 90 - lat_1
    else:
        lat_1 = 90 + abs(lat_1)

    if lat_2 > 0:
        lat_2 = 90 - lat_2
    else:
        lat_2 = 90 + abs(lat_2)

    lat_1 = deg_to_rad(lat_1)
    long_1 = deg_to_rad(long_1)
    lat_2 = deg_to_rad(lat_2)
    long_2 = deg_to_rad(long_2)

    return acos((sin(lat_1) * sin(lat_2) * cos((long_1 - long_2))) + (cos(lat_1) * cos(lat_2))) * r_earth


def deg_to_rad(angle):
    return angle * ((2 * pi) / 360)


def get_distance_between_airports(code1, code2):

    lat_1 = code1[0]
    long_1 = code1[1]
    lat_2 = code2[0]
    long_2 = code2[1]

    return dist(lat_1, lat_2, long_1, long_2)


def main():

    DUB = [53.421333, -6.270075]
    LHR = [51.4775, -0.461389]
    JFK = [40.639751, -73.778925]
    AAL = [57.092789, 9.849164]
    CDG = [49.012779, 2.55]
    SYD = [-33.943111, 151.177222]
    cities = [DUB, LHR, JFK, AAL, CDG, SYD]

    for code1 in cities:
        for code2 in cities:
            if code1 != code2:
                print(code1, code2)
                distance = get_distance_between_airports(code1, code2)
                print("The distance between", code1, "and", code2, "is", int(distance))


main()