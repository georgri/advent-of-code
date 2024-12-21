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
    if version == 0:
        if a == b:
            return "A"
        xa,ya = findChar(m, a)
        xb,yb = findChar(m, b)

        xo, yo = xb-xa, yb-ya
        res = ""
        if m[xa][ya+yo] != ' ':
            if yo < 0:
                res += '<' * abs(yo)
            else:
                res += '>' * abs(yo)

        if xo < 0:
            res +=  '^' * abs(xo)
        else:
            res += 'v' * abs(xo)
        if m[xa][ya+yo] == ' ':
            if yo < 0:
                res += '<' * abs(yo)
            else:
                res += '>' * abs(yo)
        res += 'A'
        return res
      
    if a == b:
        return "A"
    xa,ya = findChar(m, a)
    xb,yb = findChar(m, b)

    xo, yo = xb-xa, yb-ya
    res = ""
    if m[xa+xo][ya] != ' ':
        if xo < 0:
            res +=  '^' * abs(xo)
        else:
            res += 'v' * abs(xo)
    if yo < 0:
        res += '<' * abs(yo)
    else:
        res += '>' * abs(yo)
    if m[xa+xo][ya] == ' ':
        if xo < 0:
            res +=  '^' * abs(xo)
        else:
            res += 'v' * abs(xo)
    res += 'A'
    return res

def shortestKeyPad(a,b, version):
    return shortest(keyPad, a,b, version)

def shortestMovePad(a,b, version):
    return shortest(movePad, a,b, version)

from functools import cache
@cache
def moveMove(a,b, depth, version):
    presses = shortestMovePad(a,b, version)
    if depth == 0:
        return len(presses)

    moves = 0
    for x,y in zip('A' + presses, presses):
        moves += min(moveMove(x,y, depth -1, 0), moveMove(x,y, depth-1, 1))
    return moves

@cache
def move(a,b, depth, version):
    presses = shortestKeyPad(a,b, version)
    if depth == 0:
        return len(presses)

    moves = 0
    for x,y in zip('A' + presses, presses):
        moves += min(moveMove(x,y, depth -1, 0), moveMove(x,y, depth-1, 1))
    return moves


def enter(code, depth):
    moves = 0
    code = 'A' + code
    for a,b in zip(code, code[1:]):
        moves += min(move(a,b, depth, 0), move(a,b,depth,1))
    return moves



def solve(text):
    codes = read_input(text)

    res = 0
    
    for code in codes:
        moves = enter(code,2)
        print(code, moves)
        res += int(code[:-1]) * moves

    return res


print(solve(text_test))


def solve2(text):
    codes = read_input(text)

    res = 0
    
    for code in codes:
        moves = enter(code,25)
        print(code, moves)
        res += int(code[:-1]) * moves

    return res


print(solve2(text))