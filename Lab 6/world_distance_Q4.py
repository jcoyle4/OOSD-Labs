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


def get_distance_between_airports(airport_code_1, airport_code_2):
    cities = {"DUB": (53.421333, -6.270075), "LHR": (51.4775, -0.461389),
              "JFK": (40.639751, -73.778925), "AAL": (57.092789, 9.849164),
              "CDG": (49.012779, 2.55), "SYD": (-33.946111, 151.177222)}

    lat_1 = cities[airport_code_1][0]
    long_1 = cities[airport_code_1][1]
    lat_2 = cities[airport_code_2][0]
    long_2 = cities[airport_code_2][1]

    return dist(lat_1, lat_2, long_1, long_2)


def main():
    cities = ["DUB", "LHR", "JFK", "AAL", "CDG", "SYD"]
    output = []
    print("The first city is where you are. The second city is where you are going")

    for x in sorted(cities):
        final_output = output[:]
        final_output.append(x)
        for y in sorted(cities):
            if x != y:
                final_output.append(y)
                final_output.append(int(get_distance_between_airports(x, y)))
        print(final_output)

        # In the following bit of code, I tried to break out of the inner nested for loop, it didn't work
        # for x in cities:
        #     try:
        #         for y in cities:
        #             if x == y:
        #                 print(" \n TRYING TO BREAK \n ")
        #                 raise StopIteration
        #             else:
        #                 print("There is", int(get_distance_between_airports(x, y)), "km between", x, "and", y)
        #     except StopIteration:
        #         pass


main()
