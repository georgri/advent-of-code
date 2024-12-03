
text = """
1013728
23,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,733,x,x,x,x,x,x,x,x,x,x,x,x,13,17,x,x,x,x,19,x,x,x,x,x,x,x,x,x,29,x,449,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37
"""

text_test = """
939
7,13,x,x,59,x,31,19
"""

def read_input(text):
    initial = -1
    nums = []
    for line in text.split('\n'):
        if not line:
            continue

        if initial == -1:
            initial = int(line)
        else: 
            nums = [int(a) if a != 'x' else -1 for a in line.split(',')]

    return initial, nums

print(read_input(text_test))

def solve(text):
    initial, nums = read_input(text)

    minschedule = initial + max(nums)
    res = 0
    for n in nums:
        if n == -1:
            continue
        if initial %n == 0:
            return 0
        
        candidate = initial + n - initial % n
        if minschedule > candidate:
            minschedule = candidate
            res = n * (minschedule - initial)

    return res

print(solve(text))

def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm (a,b):
    return a*b//gcd(a,b)

print(lcm(15,12))

def solve2(text):
    _, nums = read_input(text)

    res = 0
    cur_lcm = 1
    for i, n in enumerate(nums):

        if n == -1:
            continue

        while (res+i) %n != 0:
            res += cur_lcm
        cur_lcm = lcm(cur_lcm, n)
        
    return res

print(solve2(text))
