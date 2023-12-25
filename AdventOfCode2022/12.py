text = """
abccccccccccccccccccaaaaaaaaacccccccccccccccccccccccccccccccccccccaaaa
abcccccccccccccccaaaaaaaaaaacccccccccccccccccccccccccccccccccccccaaaaa
abcaaccaacccccccccaaaaaaaaaacccccccccccccccccccccaaacccccccccccccaaaaa
abcaaaaaaccccccccaaaaaaaaaaaaacccccccccccccccccccaacccccccccccccaaaaaa
abcaaaaaacccaaacccccaaaaaaaaaaaccccccccccccccccccaaaccccccccccccccccaa
abaaaaaaacccaaaaccccaaaaaacaaaacccccccccccaaaacjjjacccccccccccccccccca
abaaaaaaaaccaaaaccccaaaaaaccccccaccccccccccaajjjjjkkcccccccccccccccccc
abaaaaaaaaccaaacccccccaaaccccccaaccccccccccajjjjjjkkkaaacccaaaccaccccc
abccaaacccccccccccccccaaccccaaaaaaaacccccccjjjjoookkkkaacccaaaaaaccccc
abcccaacccccccccccccccccccccaaaaaaaaccccccjjjjoooookkkkcccccaaaaaccccc
abcccccccaacccccccccccccccccccaaaacccccccijjjoooooookkkkccaaaaaaaccccc
abccaaccaaaccccccccccccccccccaaaaacccccciijjooouuuoppkkkkkaaaaaaaacccc
abccaaaaaaaccccccccccaaaaacccaacaaaccciiiiiooouuuuupppkkklllaaaaaacccc
abccaaaaaacccccccccccaaaaacccacccaaciiiiiiqooouuuuuupppkllllllacaccccc
abcccaaaaaaaacccccccaaaaaaccccaacaiiiiiqqqqoouuuxuuupppppplllllccccccc
abccaaaaaaaaaccaaaccaaaaaaccccaaaaiiiiqqqqqqttuxxxuuuppppppplllccccccc
abccaaaaaaaacccaaaaaaaaaaacccaaaahiiiqqqttttttuxxxxuuuvvpppplllccccccc
abcaaaaaaacccaaaaaaaaaaacccccaaaahhhqqqqtttttttxxxxuuvvvvvqqlllccccccc
abcccccaaaccaaaaaaaaaccccccccacaahhhqqqttttxxxxxxxyyyyyvvvqqlllccccccc
abcccccaaaccaaaaaaaacccccccccccaahhhqqqtttxxxxxxxyyyyyyvvqqqlllccccccc
SbcccccccccccaaaaaaaaaccccccccccchhhqqqtttxxxxEzzzyyyyvvvqqqmmlccccccc
abcccccccccccaaaaaaaacccaacccccccchhhppptttxxxxyyyyyvvvvqqqmmmcccccccc
abccccccccccaaaaaaaaaaccaacccccccchhhpppptttsxxyyyyyvvvqqqmmmccccccccc
abcaacccccccaaaaaaacaaaaaaccccccccchhhppppsswwyyyyyyyvvqqmmmmccccccccc
abaaaacccccccaccaaaccaaaaaaacccccccchhhpppsswwyywwyyyvvqqmmmddcccccccc
abaaaaccccccccccaaaccaaaaaaacccccccchhhpppsswwwwwwwwwvvqqqmmdddccccccc
abaaaacccccccccaaaccaaaaaaccccccccccgggpppsswwwwrrwwwwvrqqmmdddccccccc
abccccccaaaaaccaaaacaaaaaaccccccaacccggpppssswwsrrrwwwvrrqmmdddacccccc
abccccccaaaaaccaaaacccccaaccccaaaaaacggpppssssssrrrrrrrrrnmmdddaaccccc
abcccccaaaaaaccaaaccccccccccccaaaaaacggppossssssoorrrrrrrnnmdddacccccc
abcccccaaaaaaccccccccaaaaccccccaaaaacgggoooossoooonnnrrnnnnmddaaaacccc
abccccccaaaaaccccccccaaaacccccaaaaaccgggoooooooooonnnnnnnnndddaaaacccc
abccccccaaaccccccccccaaaacccccaaaaacccgggoooooooffennnnnnnedddaaaacccc
abcccccccccccccccccccaaacccccccaacccccggggffffffffeeeeeeeeeedaaacccccc
abccccccccccccccccccaaacccccaccaaccccccggfffffffffeeeeeeeeeecaaacccccc
abccccccccccccccccccaaaacccaaaaaaaaaccccfffffffaaaaaeeeeeecccccccccccc
abccccccccaacaaccccaaaaaacaaaaaaaaaaccccccccccaaaccaaaaccccccccccccccc
abccccccccaaaaacccaaaaaaaaaaacaaaaccccccccccccaaaccccaaccccccccccaaaca
abcccccccaaaaaccccaaaaaaaaaaacaaaaacccccccccccaaaccccccccccccccccaaaaa
abcccccccaaaaaacccaaaaaaaaaacaaaaaacccccccccccaaccccccccccccccccccaaaa
abcccccccccaaaaccaaaaaaaaaaaaaaccaaccccccccccccccccccccccccccccccaaaaa
"""


text_test = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


def parse(text):
    res = []

    text = text.strip()

    for i, line in enumerate(text.split('\n')):
        heights = []
        if not line:
            continue
        for j, c in enumerate(line):
            if c == "S":
                start = (i,j)
                c = "a"
            elif c == "E":
                end = (i,j)
                c = "z"
            heights.append(ord(c) - ord('a'))
        res.append(heights)

    return start, end, res


print(parse(text_test))


def get_neighbours(m, x, y, visited):
    max_x, max_y = len(m), len(m[0])
    for a, b in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        if 0 <= x + a < max_x and 0 <= y + b < max_y and (x+a, y+b) not in visited and m[x+a][y+b] <= m[x][y]+1:
            yield x+a, y+b


def bfs(m, start, target):
    visited = dict()
    visited[start] = 0

    q = [start]
    nq = []

    while q:
        #print(q, visited)
        for x, y in q:
            for a, b in get_neighbours(m, x, y, visited):
                nq.append((a, b))
                visited[(a, b)] = visited[(x, y)] + 1

                if (a, b) == target:
                    return visited[(a, b)]

        q, nq = nq, []

    return 0


def run(text):
    start, target, m = parse(text)

    res = bfs(m, start, target)

    print(res)


def run2(text):
    _, target, m = parse(text)

    res = 1 << 31
    for i, row in enumerate(m):
        for j, e in enumerate(row):
            if e == 0:
                r = bfs(m, (i,j), target)
                print(r, i, j)
                if r != 0:
                    res = min(res, r)

    print(res)


run2(text)
