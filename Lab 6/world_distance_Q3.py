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


def get_distance_between_airports():

    cities = ["DUB", "LHR", "JFK", "AAL", "CDG", "SYD"]
    latitudes = [53.421333, 51.4775, 40.639751, 57.092789, 49.012779, -33.946111]
    longitudes = [-6.270075, -0.461389, -73.778925, 9.849164, 2.55, 151.177222]
    output = []

    print("The first city is where you are. The second city is where you are going")

    for x in range(0, len(latitudes)):
        final_output = output[:]
        final_output.append(cities[x])
        lat_1 = latitudes[x]
        long_1 = longitudes[x]
        for y in range(0, len(latitudes)):
            if x != y:
                final_output.append(cities[y])
                lat_2 = latitudes[y]
                long_2 = longitudes[y]
                distance = dist(lat_1, lat_2, long_1, long_2)
                final_output.append(int(distance))
                # print("The distance between", cities[x], "and", cities[y], "is", distance)
        print(final_output)
    return 0


def main():
    get_distance_between_airports()

main()