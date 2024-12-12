text = """
4329 385 0 1444386 600463 19 1 56615
"""

text_test = """
125 17
"""

def read_input(text):
    for line in text.split('\n'):
        if not line:
            continue

        return list(map(int, line.split()))
    
    return []


print(read_input(text_test))


def solve(text):
    prev = read_input(text)

    for i in range(25):
        cur = []

        for k in prev:
            if k == 0:
                cur.append(1)
            elif len(str(k)) %2 == 0:
                s = str(k)
                mid = len(s) // 2
                a,b = s[:mid], s[mid:]
                cur.append(int(a))
                cur.append(int(b))
            else:
                cur.append(k*2024)
        
        prev = cur
        print(i, len(prev))

    return len(prev)

print(solve(text))

from functools import cache

@cache
def calc(k, depth):
    if depth == 0: # 1?
        return 1
    
    if k == 0:
        return calc(1, depth-1)
    elif len(str(k)) %2 == 0:
        s = str(k)
        mid = len(s) // 2
        a,b = s[:mid], s[mid:]
        return calc(int(a), depth-1) + calc(int(b), depth-1)
    else:
        return calc(k*2024, depth-1)


def solve2(text):
    inp = read_input(text)

    res = 0
    for k in inp:
        res += calc(k, 75)

    return res

print(solve2(text))