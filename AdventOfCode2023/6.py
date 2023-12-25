

text = '''
Time:        40     82     84     92
Distance:   233   1011   1110   1487
'''

text_test = '''
Time:      7  15   30
Distance:  9  40  200
'''


def read(text):
    res = []

    times = []
    dists = []

    for line in text.split('\n'):
        if not line:
            continue

        nums = line.split(':')[1].strip()
        nums = [int(i) for i in nums.split(' ') if i]
        if 'Time' in line:
            times = nums
        elif 'Distance' in line:
            dists = nums

    for a,b in zip(times, dists):
        res.append((a,b))

    return res


def read2(text):

    time = 0
    dist = 0
    for line in text.split('\n'):
        if not line:
            continue

        nums = line.split(':')[1].strip()
        nums = nums.replace(' ', '')
        nums = int(nums)
        if 'Time' in line:
            time = nums
        elif 'Distance' in line:
            dist = nums

    return (time, dist)


print(read2(text_test))


def solve(text):
    races = read(text)

    res = 1

    for time, distance in races:
        ways = 0
        for delay in range(time):
            cur_dist = (time - delay) * delay
            if cur_dist > distance:
                ways += 1

        res = res * ways

    print (res)


#solve(text)


def solve2(text):
    race = read2(text)


    time, distance = race

    ways = 0
    for delay in range(time):
        cur_dist = (time - delay) * delay
        if cur_dist > distance:
            ways += 1

    print(ways)


solve2(text)
