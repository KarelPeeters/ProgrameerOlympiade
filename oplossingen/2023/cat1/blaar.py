from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    c, _ = readints()
    deltas = readints()

    output = f"{case + 1}"
    curr = 0
    for d in deltas:
        curr += d
        if curr <= 0.8 * c:
            output += " g"
        elif curr <= c:
            output += " o"
        else:
            output += " r"

    print(output)
