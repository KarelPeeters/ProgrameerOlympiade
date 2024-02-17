import math

from oplossingen.lib import readline, readints

cases = int(readline())


def add(a, b):
    at, an = a
    bt, bn = b

    ct = at * bn + bt * an
    cn = an * bn

    g = math.gcd(ct, cn)
    return ct // g, cn // g


for case in range(cases):
    # input
    _ = int(readline())
    events = readints()

    # print(persons)

    # calc
    present = set()
    discounts = [(0, 1)] * (len(events)//2)

    for p in events:
        p -= 1
        if p in present:
            present.remove(p)
        else:
            dis = (1, 2 ** (len(present)))
            for c in present:
                discounts[c] = add(discounts[c], dis)
            present.add(p)
            present.add(p)

    # output
    for i in range(len(events) // 2):
        dt, dn = discounts[i]
        if dt / dn > 0.73:
            dt, dn = (73, 100)

        if dt == 0:
            s = "0"
        else:
            s = f"{dt}/{dn}"

        print(f"{case+1} {i+1} {s}")

    # print(persons)
    # print(discounts)
