
text = """
Monkey 0:
  Starting items: 71, 86
  Operation: new = old * 13
  Test: divisible by 19
    If true: throw to monkey 6
    If false: throw to monkey 7

Monkey 1:
  Starting items: 66, 50, 90, 53, 88, 85
  Operation: new = old + 3
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 4

Monkey 2:
  Starting items: 97, 54, 89, 62, 84, 80, 63
  Operation: new = old + 6
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 1

Monkey 3:
  Starting items: 82, 97, 56, 92
  Operation: new = old + 2
  Test: divisible by 5
    If true: throw to monkey 6
    If false: throw to monkey 0

Monkey 4:
  Starting items: 50, 99, 67, 61, 86
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 5
    If false: throw to monkey 3

Monkey 5:
  Starting items: 61, 66, 72, 55, 64, 53, 72, 63
  Operation: new = old + 4
  Test: divisible by 11
    If true: throw to monkey 3
    If false: throw to monkey 0

Monkey 6:
  Starting items: 59, 79, 63
  Operation: new = old * 7
  Test: divisible by 17
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 7:
  Starting items: 55
  Operation: new = old + 7
  Test: divisible by 3
    If true: throw to monkey 2
    If false: throw to monkey 1
"""

text_test = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""

def last_int(s):
    return int(s.split(" ")[-1])


def get_func(s):
    if "old" in s:
        return lambda x: x*x
    elif "+" in s:
        arg = int(s.split(" ")[-1])
        return lambda x: x + arg
    elif "*" in s:
        arg = int(s.split(" ")[-1])
        return lambda x: x * arg

    return None


def parse(text):
    items = []
    tests = []
    ops = []

    for line in text.split('\n'):
        if not line:
            continue
        split = line.split(': ')
        if len(split) < 2:
            continue
        after_colon = split[1]
        if "Starting" in line:
            items.append(list(map(int, after_colon.split(', '))))
        elif "Test" in line:
            tests.append([last_int(after_colon)])
        elif "If true" in line or "If false" in line:
            tests[-1].append(last_int(after_colon))
        elif "= old" in line:
            ops.append(get_func(after_colon.split("= old ")[-1]))

    return items, tests, ops


print(parse(text_test))


def simulate(items, tests, ops):
    res = [0] * len(items)

    for _ in range(20):
        for i, (curitems, test, op) in enumerate(zip(items, tests, ops)):
            res[i] += len(curitems)

            for worry in curitems:
                new_worry = op(worry)
                new_worry = new_worry // 3
                if new_worry % test[0] == 0:
                    new_monkey = test[1]
                else:
                    new_monkey = test[2]

                items[new_monkey].append(new_worry)

            curitems[:] = []

    return res


def run(text):
    items, tests, ops = parse(text)

    new_items = simulate(items, tests, ops)

    print(new_items)

    new_items.sort()

    print(new_items[-1] * new_items[-2])

def nod(a,b):
    if b == 0:
        return a
    return nod(b, a % b)


def nok(a, b):
    return a * b // nod(a,b)


def simulate2(items, tests, ops):
    res = [0] * len(items)

    max_mult = 1
    for test in tests:
        max_mult = nok(max_mult, test[0])

    for _ in range(10000):
        for i, (curitems, test, op) in enumerate(zip(items, tests, ops)):
            res[i] += len(curitems)

            for worry in curitems:
                new_worry = op(worry)
                new_worry = new_worry % max_mult
                if new_worry % test[0] == 0:
                    new_monkey = test[1]
                else:
                    new_monkey = test[2]

                items[new_monkey].append(new_worry)

            curitems[:] = []

    return res


def run2(text):
    items, tests, ops = parse(text)

    new_items = simulate2(items, tests, ops)

    print(new_items)

    new_items.sort()

    print(new_items[-1] * new_items[-2])


run2(text)
