from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    # parse
    wx, wy, hx, hy = readints()

    eq = (wx + wy) // 2

    if wx > eq:
        nx = min(wx, max(0, eq, hx, hy))
        ny = wy - (nx - wx)
    elif wy > eq:
        ny = min(wy, max(0, eq, hy, hx))
        nx = wx - (ny - wy)
    else:
        nx, ny = eq, eq

    if nx == ny:
        print(f"{case+1} gelijk")
    else:
        print(f"{case+1} {nx} {ny}")



