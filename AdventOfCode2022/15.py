text = """
Sensor at x=2332081, y=2640840: closest beacon is at x=2094728, y=2887414
Sensor at x=3048293, y=3598671: closest beacon is at x=3872908, y=3598272
Sensor at x=2574256, y=3973583: closest beacon is at x=2520711, y=4005929
Sensor at x=3011471, y=2514567: closest beacon is at x=2999559, y=2558817
Sensor at x=3718881, y=2593817: closest beacon is at x=2999559, y=2558817
Sensor at x=2388052, y=2201955: closest beacon is at x=2163809, y=1961540
Sensor at x=3783125, y=3897169: closest beacon is at x=3872908, y=3598272
Sensor at x=1864613, y=3918152: closest beacon is at x=2520711, y=4005929
Sensor at x=2850099, y=689863: closest beacon is at x=3231146, y=2000000
Sensor at x=3431652, y=2328669: closest beacon is at x=3231146, y=2000000
Sensor at x=3480248, y=3999492: closest beacon is at x=3872908, y=3598272
Sensor at x=455409, y=3347614: closest beacon is at x=-399822, y=4026621
Sensor at x=2451938, y=2950107: closest beacon is at x=2094728, y=2887414
Sensor at x=1917790, y=3194437: closest beacon is at x=2094728, y=2887414
Sensor at x=3947393, y=3625984: closest beacon is at x=3872908, y=3598272
Sensor at x=1615064, y=2655330: closest beacon is at x=2094728, y=2887414
Sensor at x=3630338, y=1977851: closest beacon is at x=3231146, y=2000000
Sensor at x=3878266, y=3019867: closest beacon is at x=3872908, y=3598272
Sensor at x=2837803, y=2395749: closest beacon is at x=2999559, y=2558817
Sensor at x=3979396, y=3697962: closest beacon is at x=3872908, y=3598272
Sensor at x=109399, y=250528: closest beacon is at x=929496, y=-688981
Sensor at x=2401381, y=3518884: closest beacon is at x=2520711, y=4005929
Sensor at x=3962391, y=71053: closest beacon is at x=5368730, y=-488735
Sensor at x=1751119, y=97658: closest beacon is at x=929496, y=-688981
Sensor at x=2932155, y=2967347: closest beacon is at x=2999559, y=2558817
Sensor at x=3326630, y=2845463: closest beacon is at x=2999559, y=2558817
Sensor at x=3959042, y=1734156: closest beacon is at x=3231146, y=2000000
Sensor at x=675279, y=1463916: closest beacon is at x=2163809, y=1961540
Sensor at x=3989603, y=3500749: closest beacon is at x=3872908, y=3598272
Sensor at x=1963470, y=2288355: closest beacon is at x=2163809, y=1961540
"""

text_test = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""


def get_coord(s):
    return list(map(int, s.replace(" x=", " ").replace(", y=", " ").split(" ")[-2:]))


def parse(text):
    sensors = []
    beacons = []

    for line in text.split('\n'):
        if not line:
            continue

        sensor, beacon = line.split(":")

        s, b = get_coord(sensor), get_coord(beacon)

        sensors.append((s[1], s[0]))
        beacons.append((b[1], b[0]))

    return sensors, beacons


print(parse(text_test))


def manhattan(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])


def row_at_dist(s, row, dist):
    x, y = s

    mindist = abs(x - row)

    offset = dist - mindist
    if offset < 0:
        return 0, 0

    return y - offset, y + offset + 1


def run(text, row):
    sensors, beacons = parse(text)

    visited = set()

    for s, b in zip(sensors, beacons):
        dist = manhattan(s, b)

        f, t = row_at_dist(s, row, dist)
        # print(s, b, cells)
        for i in range(f, t + 1):
            if (row, i) == b:
                print("BEACON", b)
                continue
            if i not in visited:
                visited.add(i)

    print(len(visited))
    # print(visited)


def run_test():
    return run(text_test, 10)


def run_prod():
    return run(text, 2000000)


def run2(text, maxcoord):
    sensors, beacons = parse(text)

    sensors_enriched = []
    for s, b in zip(sensors, beacons):
        sensors_enriched.append((s, manhattan(s, b)))

    sensors_enriched.sort(key=lambda x: x[0][1])
    sensors = sensors_enriched

    beacons = set(beacons)
    for row in range(0, maxcoord + 1):
        ranges = []
        max_prev_t = -1
        for s, dist in sensors:

            f, t = row_at_dist(s, row, dist)
            if f == t:
                continue
            ranges.append((f, t))

        ranges.sort()
        for f, t in ranges:
            if f > max_prev_t:
                if (row, f - 1) not in beacons and f-1 >= 0:
                    print(f - 1, row, (f-1) * 4000000 + row)

            #print(row, ": ", max_prev_t, f, t)
            max_prev_t = max(max_prev_t, t)


def run_test2():
    return run2(text_test, 20)


# 2655411 3166538
def run_prod2():
    return run2(text, 4000000)


run_prod2()
