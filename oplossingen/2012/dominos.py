H = 7
W = 8

ALL_TILES = {
    (j, i)
    for i in range(6 + 1)
    for j in range(i + 1)
}
ALL_POS = {
    (x, y)
    for x in range(W)
    for y in range(H)
}


# f = open("/home/karel/Documents/ProgrameerOlympiade/opgaves/2012/cat3/dominos/voorbeeld.invoer")
# def input():
#     return f.readline().strip()


def main():
    t = int(input())

    for ti in range(t):
        grid = []
        if ti != 0:
            assert input() == ""
        for _ in range(7):
            grid.append(list(map(int, input().split(" "))))

        def f(free: set, tiles: set):
            curr = None
            for y in range(H):
                for x in range(W):
                    if (x, y) in free:
                        curr = (x, y)
                        break
                if curr:
                    break
            if curr is None:
                return 1
            (x, y) = curr

            free.remove(curr)

            total = 0

            # try hor
            other = (x + 1, y)
            if other in free:
                tile = (grid[y][x], grid[y][x + 1])
                tile = (min(tile), max(tile))

                if tile in tiles:
                    free.remove(other)
                    tiles.remove(tile)
                    total += f(free, tiles)
                    free.add(other)
                    tiles.add(tile)

            # try ver
            other = (x, y + 1)
            if other in free:
                tile = (grid[y][x], grid[y + 1][x])
                tile = (min(tile), max(tile))

                if tile in tiles:
                    free.remove(other)
                    tiles.remove(tile)
                    total += f(free, tiles)
                    free.add(other)
                    tiles.add(tile)

            free.add(curr)
            return total

        print(f(set(ALL_POS), set(ALL_TILES)))
        # break


if __name__ == '__main__':
    main()
