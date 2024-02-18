from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    _, v = readints()
    scores = readints()

    # print(v, scores)

    best = max(scores[:v])
    for i, s in enumerate(scores[v:]):
        i += v
        if i == len(scores) - 1 or s >= best:
            print(f"{case + 1} {i + 1} {s}")
            break
