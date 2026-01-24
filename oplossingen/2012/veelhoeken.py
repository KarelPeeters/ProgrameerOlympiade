# f = open("/home/karel/Documents/ProgrameerOlympiade/opgaves/2012/cat3/veelhoeken/voorbeeld.invoer")
#
#
# def input():
#     return f.readline().strip()


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        lines = []
        mx = 0
        my = 0
        for _ in range(n):
            x1, y1, x2, y2 = map(int, input().split(" "))
            mx = max(mx, x1 + 1, x2 + 1)
            my = max(my, y1 + 1, y2 + 1)
            lines.append((x1, y1, x2, y2))

        grid = [[False] * 2 * mx for _ in range(2 * my)]
        grid_t = [[False] * 2 * my for _ in range(2 * mx)]
        for x1, y1, x2, y2 in lines:
            if x1 == x2:
                for y in range(2 * y1, 2 * y2 + 1):
                    grid[y][2 * x1] = True
                    grid_t[2 * x1][y] = True
            else:
                assert y1 == y2
                for x in range(2 * x1, 2 * x2 + 1):
                    grid[2 * y1][x] = True
                    grid_t[x][2 * y1] = True

        # for g in reversed(grid):
        #     for d in g:
        #         print([".", "#"][int(d)], end="")
        #     print()

        c = 0
        for x in range(mx):
            for y in range(my):
                for w in range(1, mx - x):
                    for h in range(1, my - y):
                        if all(grid[2 * y][2 * x:2 * x + 2 * w]) and all(
                                grid[2 * y + 2 * h][2 * x:2 * x + 2 * w]) and all(
                                grid_t[2 * x][2 * y:2 * y + 2 * h]) and all(
                                grid_t[2 * x + 2 * w][2 * y:2 * y + 2 * h]):
                            # print(x, y, w, h)
                            c += 1

        print(c)
        # break


if __name__ == '__main__':
    main()
