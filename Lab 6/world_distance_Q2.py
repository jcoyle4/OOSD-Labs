from math import pi, acos, sin, cos

r_earth = float(6371)


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


def main():

    cities = {"DUB": (53.421333, -6.270075), "LHR": (51.4775, -0.461389),
              "JFK": (40.639751, -73.778925), "AAL": (57.092789, 9.849164),
              "CDG": (49.012779, 2.55), "SYD": (-33.946111, 151.177222)}

    for item1 in sorted(cities):
        latitude_1 = cities[item1][0]
        longitude_1 = cities[item1][1]

        for item2 in sorted(cities):
            if item1 != item2:
                latitude_2 = cities[item2][0]
                longitude_2 = cities[item2][1]

                distance = dist(latitude_1, latitude_2, longitude_1, longitude_2)

                print("The distance between", item1, "and", item2, "is", int(distance))

main()