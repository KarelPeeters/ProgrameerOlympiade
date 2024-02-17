from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    _, *row = readints()
    # print(row)

    a, b, c = row[:3]
    pairs = zip(row[:-1], row[1:])

    # reken
    factor = b // a
    delta = b - a
    # print(f"factor: {factor}, delta: {delta}")

    if all(x * factor == y for x, y in pairs):
        print(f"{case+1} meetkundig met stap {factor}: {row[-1] * factor}")
    elif all(x + delta == y for x, y in pairs):
        print(f"{case+1} rekenkundig met stap {delta}: {row[-1] + delta}")
    else:
        print(f"{case+1} geen van beide")
