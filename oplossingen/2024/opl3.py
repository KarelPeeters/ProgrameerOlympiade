from typing import List


def readline(f=None) -> str:
    if f is None:
        return input().strip()
    else:
        return f.readline().strip()


def readint(f=None) -> int:
    return int(readline(f))


def readints(f=None) -> List[int]:
    line = readline(f)
    if not line:
        return []
    return [int(x) for x in line.split(" ")]


def ortho_neighbors(h, w, y, x):
    mid = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    return [(ny, nx) for ny, nx in mid if 0 <= ny < h and 0 <= nx < w]


cases = readint()

for case in range(cases):
    n = readint()
    n_cards, cards = readline().split(" ")

    # (colorbool, typebool, amount)
    cards = []

    for card in cards:
        type, num = card
        print(f"t={type} n={num}")




    # print(result)
    print(" ".join(str(x) for x in result))
