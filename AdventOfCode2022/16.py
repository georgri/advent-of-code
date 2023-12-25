text = """
Valve MU has flow rate=0; tunnels lead to valves VT, LA
Valve TQ has flow rate=0; tunnels lead to valves HU, SU
Valve YH has flow rate=0; tunnels lead to valves CN, BN
Valve EO has flow rate=0; tunnels lead to valves IK, CN
Valve MH has flow rate=0; tunnels lead to valves GG, HG
Valve RJ has flow rate=0; tunnels lead to valves AA, RI
Valve XZ has flow rate=0; tunnels lead to valves PX, VT
Valve UU has flow rate=0; tunnels lead to valves DT, XG
Valve KV has flow rate=13; tunnels lead to valves HN, CV, PE, XD, TA
Valve SU has flow rate=19; tunnels lead to valves TQ, HF, OL, SF
Valve BB has flow rate=0; tunnels lead to valves NS, HR
Valve RI has flow rate=4; tunnels lead to valves ML, EE, TZ, RJ, PE
Valve TZ has flow rate=0; tunnels lead to valves VT, RI
Valve LY has flow rate=0; tunnels lead to valves EE, RP
Valve PX has flow rate=0; tunnels lead to valves XZ, JQ
Valve VH has flow rate=0; tunnels lead to valves DT, TA
Valve HN has flow rate=0; tunnels lead to valves KV, LR
Valve LR has flow rate=0; tunnels lead to valves HR, HN
Valve NJ has flow rate=0; tunnels lead to valves QF, JC
Valve AM has flow rate=0; tunnels lead to valves OJ, AA
Valve FM has flow rate=0; tunnels lead to valves VT, RP
Valve VT has flow rate=5; tunnels lead to valves IP, XZ, TZ, FM, MU
Valve HF has flow rate=0; tunnels lead to valves NR, SU
Valve HR has flow rate=11; tunnels lead to valves BB, KO, LR
Valve WX has flow rate=0; tunnels lead to valves CN, IP
Valve PE has flow rate=0; tunnels lead to valves KV, RI
Valve QF has flow rate=17; tunnels lead to valves YI, NJ
Valve EE has flow rate=0; tunnels lead to valves LY, RI
Valve UH has flow rate=25; tunnel leads to valve YI
Valve CV has flow rate=0; tunnels lead to valves KV, NS
Valve SF has flow rate=0; tunnels lead to valves YN, SU
Valve RP has flow rate=3; tunnels lead to valves HG, FM, OJ, IK, LY
Valve XD has flow rate=0; tunnels lead to valves IL, KV
Valve GG has flow rate=12; tunnels lead to valves ML, IL, MH, OL, KA
Valve XG has flow rate=0; tunnels lead to valves LI, UU
Valve YA has flow rate=21; tunnels lead to valves UJ, GQ
Valve OL has flow rate=0; tunnels lead to valves GG, SU
Valve AN has flow rate=0; tunnels lead to valves AA, IX
Valve LI has flow rate=15; tunnel leads to valve XG
Valve GQ has flow rate=0; tunnels lead to valves YA, KO
Valve HU has flow rate=0; tunnels lead to valves TQ, DT
Valve OJ has flow rate=0; tunnels lead to valves RP, AM
Valve YN has flow rate=0; tunnels lead to valves SF, JQ
Valve ML has flow rate=0; tunnels lead to valves RI, GG
Valve UJ has flow rate=0; tunnels lead to valves YA, NS
Valve IX has flow rate=0; tunnels lead to valves AN, JQ
Valve JC has flow rate=0; tunnels lead to valves JQ, NJ
Valve TA has flow rate=0; tunnels lead to valves KV, VH
Valve DT has flow rate=16; tunnels lead to valves UU, HU, KA, VH
Valve NR has flow rate=0; tunnels lead to valves HF, CN
Valve YI has flow rate=0; tunnels lead to valves QF, UH
Valve AA has flow rate=0; tunnels lead to valves AM, AN, BN, LA, RJ
Valve BN has flow rate=0; tunnels lead to valves AA, YH
Valve KA has flow rate=0; tunnels lead to valves GG, DT
Valve IL has flow rate=0; tunnels lead to valves GG, XD
Valve CN has flow rate=7; tunnels lead to valves YH, EO, WX, NR, OM
Valve IP has flow rate=0; tunnels lead to valves WX, VT
Valve OM has flow rate=0; tunnels lead to valves CN, JQ
Valve KO has flow rate=0; tunnels lead to valves GQ, HR
Valve LA has flow rate=0; tunnels lead to valves AA, MU
Valve JQ has flow rate=6; tunnels lead to valves IX, JC, PX, YN, OM
Valve IK has flow rate=0; tunnels lead to valves EO, RP
Valve HG has flow rate=0; tunnels lead to valves MH, RP
Valve NS has flow rate=23; tunnels lead to valves CV, BB, UJ
"""

text_test = """
Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II
"""


def parse(text):
    indices = dict()
    rates = []
    adjacent = []

    for line in text.split('\n'):
        if not line:
            continue

        fields = line.replace("rate=", "").replace(';', '').replace(',', '').split(' ')
        name = fields[1]
        if name == 'AA':
            start = len(rates)
        rate = int(fields[4])
        adj = fields[9:]

        indices[name] = len(rates)
        rates.append(rate)
        adjacent.append(adj)

    neighbors = []

    for adj in adjacent:
        converted = list(map(lambda x: indices[x], adj))
        neighbors.append(converted)

    return rates, neighbors, start


print(parse(text_test))


def setbit(i, bit):
    return i | (1 << bit)


def unsetbit(i, bit):
    return i ^ (1 << bit)


def checkbit(i, bit):
    return i & (1 << bit) != 0


# добавить memoization
memo = dict()


# recursion of depth 30 go!
def backtrack(memo, rates, neighbors, cur, minutes, openedvalves):
    # base condition: if 0 minutes => return 0
    if minutes <= 1:
        return 0

    if minutes == 2:
        if checkbit(openedvalves, cur):
            return 0
        return rates[cur]

    memokey = (cur, minutes, openedvalves)
    if memokey in memo:
        # print("CACHED: ", memokey, memo[memokey])
        return memo[memokey]

    # try all the possible actions, then undo;
    # return max result at the end

    maxres = 0

    # можем куда-то сходить без открытия вентиля
    for adj in neighbors[cur]:
        # пытаемся сходить в adj
        maxres = max(maxres, backtrack(memo, rates, neighbors, adj, minutes - 1, openedvalves))

    # можем открыть вентиль
    if rates[cur] > 0 and not checkbit(openedvalves, cur):
        openedvalves = setbit(openedvalves, cur)

        # print("BEFORE OPENING VALVE: ", memokey, maxres)

        maxres = max(maxres,
                     rates[cur] * (minutes - 1) + backtrack(memo, rates, neighbors, cur, minutes - 1, openedvalves))

        # print("OPENED VALVE: ", memokey, maxres)

        openedvalves = unsetbit(openedvalves, cur)

    memo[memokey] = maxres
    # print(memokey, maxres)

    return maxres


def run(text):
    rates, neighbors, start = parse(text)

    res = backtrack(memo, rates, neighbors, start, 30, 0)

    print(res)


def run2(text):
    rates, neighbors, start = parse(text)

    countvalves = 0
    for r in rates:
        if r > 0:
            countvalves += 1

    print(countvalves)

    # пронумеровать все rates > 0 от 0 до 15
    nonemptyrateindices = []
    for i, r in enumerate(rates):
        if r > 0:
            nonemptyrateindices.append(i)

    bufferedresults = []
    for i in range (0, 1 << countvalves):
        rates_new = []
        memo = dict()
        rates_new[:] = rates[:]
        countv = 0
        for j in range(countvalves):
            # подготовить rates
            if not checkbit(i, j):
                rates_new[nonemptyrateindices[j]] = 0
            else:
                countv += 1

        #print(rates_new)

        res = backtrack(memo, rates_new, neighbors, start, 26, 0)

        bufferedresults.append(res)
        print("#", i, "=", res)

    maxres = 0
    for i, res in enumerate(bufferedresults):

        inverted = i
        # инвертировать i
        for j in range(countvalves):
            inverted = unsetbit(inverted, j)

        invertedres = res + bufferedresults[inverted]
        if invertedres > maxres:
            # print("new max is ", i, inverted)
            maxres = invertedres

    print(maxres)


run2(text)
