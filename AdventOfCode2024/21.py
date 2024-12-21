text = """
341A
083A
802A
973A
780A
"""

text_test = """
029A
980A
179A
456A
379A
"""

def read_input(text):
    res = []
    for line in text.split('\n'):
        if not line:
            continue
        res.append(line)

    return res


print(read_input(text_test))

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""

keyPad = ["789", "456", "123"," 0A"]
movePad = [" ^A", "<v>"]

def findChar(m, c):
    for i, row in enumerate(m):
        for j, col in enumerate(row):
            if c == col:
                return i,j
    print(m, c)
    return None
        
def shortest(m, a,b, version):
    if a == b:
        return "A"
    xa,ya = findChar(m, a)
    xb,yb = findChar(m, b)
    xo, yo = xb-xa, yb-ya
    res = ""

    xs = "^v"[int(xo >= 0)] * abs(xo)
    ys = "<>"[int(yo >= 0)] * abs(yo)

    if version == 0 and m[xa+xo][ya] != ' ' or m[xa][ya+yo] == ' ':
        return xs+ys+'A'
      
    return ys+xs+'A'

def shortestKeyPad(a,b, version):
    return shortest(keyPad, a,b, version)

def shortestMovePad(a,b, version):
    return shortest(movePad, a,b, version)

from functools import cache

@cache
def move(a,b, depth, version, initial):
    if initial:
        f = shortestKeyPad
    else:
        f = shortestMovePad
    presses = f(a,b, version)
    if depth == 0:
        return len(presses)

    return enter(presses, depth-1, False)

@cache
def enter(code, depth, initial):
    moves = 0
    for a,b in zip('A' + code, code):
        moves += min(move(a,b, depth, 0, initial), move(a,b,depth,1, initial))
    return moves



def solve(text):
    codes = read_input(text)

    res = 0
    
    for code in codes:
        moves = enter(code,2, True)
        print(code, moves)
        res += int(code[:-1]) * moves

    return res


print(solve(text))


def solve2(text):
    codes = read_input(text)

    res = 0
    
    for code in codes:
        moves = enter(code,25, True)
        print(code, moves)
        res += int(code[:-1]) * moves

    return res


print(solve2(text))