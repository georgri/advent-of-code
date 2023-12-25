text = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 9 clay. Each geode robot costs 3 ore and 9 obsidian.
Blueprint 2: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 3: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 16 clay. Each geode robot costs 2 ore and 9 obsidian.
Blueprint 4: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 4 ore and 16 obsidian.
Blueprint 5: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 16 clay. Each geode robot costs 2 ore and 15 obsidian.
Blueprint 6: Each ore robot costs 2 ore. Each clay robot costs 2 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 2 ore and 14 obsidian.
Blueprint 7: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 7 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 8: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 15 obsidian.
Blueprint 9: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 7 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 10: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 2 ore and 11 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 11: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 20 clay. Each geode robot costs 2 ore and 12 obsidian.
Blueprint 12: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 20 clay. Each geode robot costs 2 ore and 8 obsidian.
Blueprint 13: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 4 ore and 9 obsidian.
Blueprint 14: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 18 clay. Each geode robot costs 3 ore and 8 obsidian.
Blueprint 15: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 9 clay. Each geode robot costs 3 ore and 15 obsidian.
Blueprint 16: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 11 clay. Each geode robot costs 2 ore and 16 obsidian.
Blueprint 17: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 13 clay. Each geode robot costs 3 ore and 15 obsidian.
Blueprint 18: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 16 clay. Each geode robot costs 3 ore and 20 obsidian.
Blueprint 19: Each ore robot costs 2 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 19 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 20: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 16 clay. Each geode robot costs 2 ore and 15 obsidian.
Blueprint 21: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 7 clay. Each geode robot costs 2 ore and 19 obsidian.
Blueprint 22: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 14 clay. Each geode robot costs 3 ore and 17 obsidian.
Blueprint 23: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 8 clay. Each geode robot costs 2 ore and 8 obsidian.
Blueprint 24: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 7 clay. Each geode robot costs 4 ore and 17 obsidian.
Blueprint 25: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 16 clay. Each geode robot costs 3 ore and 9 obsidian.
Blueprint 26: Each ore robot costs 4 ore. Each clay robot costs 3 ore. Each obsidian robot costs 4 ore and 15 clay. Each geode robot costs 4 ore and 9 obsidian.
Blueprint 27: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 2 ore and 20 clay. Each geode robot costs 4 ore and 7 obsidian.
Blueprint 28: Each ore robot costs 3 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 17 clay. Each geode robot costs 4 ore and 8 obsidian.
Blueprint 29: Each ore robot costs 3 ore. Each clay robot costs 4 ore. Each obsidian robot costs 3 ore and 12 clay. Each geode robot costs 3 ore and 17 obsidian.
Blueprint 30: Each ore robot costs 4 ore. Each clay robot costs 4 ore. Each obsidian robot costs 4 ore and 5 clay. Each geode robot costs 2 ore and 10 obsidian.
"""

text_test = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
"""

text_test2 = """
Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
"""

def parse(text):
    res = []

    for line in text.split('\n'):
        if not line:
            continue

        ore, clay, obsidian, geode, _ = line.split('.')

        costs = []
        costs.append([int(ore.split(' ')[6])])

        clay = clay.strip().split(' ')
        costs.append([int(clay[4])])

        obsidian = obsidian.strip().split(' ')
        costs.append([int(obsidian[4]), int(obsidian[7])])

        geode = geode.strip().split(' ')
        costs.append([int(geode[4]), 0, int(geode[7])])

        res.append(costs)

    return res


print(parse(text_test))


def max_robots(cost, resources):
    res = -1
    for a, b in zip(cost, resources):
        if a == 0:
            continue
        if res == -1 or b // a < res:
            res = b // a

    return res + 1


def unbuild_robot(cost, robots, resources, kind):
    if kind == -1:
        return

    for j in range(len(cost)):
        resources[j] += cost[j]

    robots[kind] -= 1


def build_robot(cost, robots, resources, kind):
    if kind == -1:
        return True

    robots[kind] += 1

    possible = True

    for j in range(len(cost)):
        resources[j] -= cost[j]
        if resources[j] < 0:
            possible = False

    if not possible: # возвращаем назад
        unbuild_robot(cost, robots, resources, kind)

    return possible

# ПРОЦЕСС НЕПРАВИЛЬНЫЙ!
# СНАЧАЛА НАЧАТЬ СТРОИТЬ РОБОТА, ПОТОМ ДОБЫТЬ РЕСУРС СТАРЫМИ РОБОТАМИ, НОВЫЙ РОБОТ ПОСТРОЕН К СЛЕДУЮЩЕМУ ХОДУ!
def backtrack(costs, robots, resources, minutes_left, memo):
    if minutes_left <= 1:
        return 0

    if minutes_left == 2 and resources[2] < costs[3][2]:
        return 0

    if minutes_left == 3 and resources[2] + robots[2] < costs[3][2]:
        return 0

    if minutes_left == 4 and resources[2] + robots[2] * 2 + 1 < costs[3][2]:
        return 0

    key = (tuple(robots[:3]), tuple(resources[:3]), minutes_left)
    if key in memo:
        return memo[key]

    # print(robots, resources, minutes_left)

    maxres = 0

    # пробовать строительство всех вариантов роботов, которые возможно построить при текущем кол-ве ресурсов
    # ну тупо 4 цикла можно
    # ФАБРИКА МОЖЕТ ПРОИЗВЕСТИ ЛИШЬ ОДНОГО РОБОТА В МИНУТУ, ЙОУ!!!!
    for robot_kind in range(-1, 4):
        # # предполагаем, что не нужно строить робота рудника, если уже построили глиняного робота
        if robots[1] > 0 and robot_kind == 0:
            continue

        possible = build_robot(costs[robot_kind], robots, resources, robot_kind)
        if not possible:
            continue

        # добываем ресурсы
        for i in range(len(robots)):
            resources[i] += robots[i]
            if i == robot_kind:
                resources[i] -= 1

        if robot_kind == 3:
            maxres = max(maxres, minutes_left-1 + backtrack(costs, robots, resources, minutes_left - 1, memo))
        else:
            maxres = max(maxres, backtrack(costs, robots, resources, minutes_left - 1, memo))

        unbuild_robot(costs[robot_kind], robots, resources, robot_kind)

        # возвращаем ресурсы на место
        for i in range(len(robots)):
            resources[i] -= robots[i]

    memo[key] = maxres

    return maxres


def run(text):
    # идея - сделать backtracking, а потом сверху бахнуть memo

    cost_arrays = parse(text)

    result = 0
    for i, costs in enumerate(cost_arrays):
        res = backtrack(costs, [1, 0, 0, 0], [0, 0, 0, 0], 24, dict())
        print(i+1, res)
        result += (i+1) * res

    print(result)

#1220 - too low
#run(text)

# pypy was fast enough :)
def run2(text):
    # идея - сделать backtracking, а потом сверху бахнуть memo

    cost_arrays = parse(text)[:3]

    result = 1
    for i, costs in enumerate(cost_arrays):
        res = backtrack(costs, [1, 0, 0, 0], [0, 0, 0, 0], 32, dict())
        print(i+1, res)
        result *= res

    print(result)

run2(text)
