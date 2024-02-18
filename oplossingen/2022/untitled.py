from oplossingen.fenwick import FenwickIndexTree
from oplossingen.lib import readline, readints

cases = int(readline())

for case in range(cases):
    # parse
    n = int(readline())
    a = readints()
    assert len(a) == n

    # calc
    tree = FenwickIndexTree(n)

    sort_pos_to_a_pos = sorted(range(n), key=lambda i: a[i])
    a_pos_to_sort_pos = [-1] * n
    for x, y in enumerate(sort_pos_to_a_pos):
        a_pos_to_sort_pos[y] = x

    result_rev = []

    for i in reversed(range(n)):
        ai = a_pos_to_sort_pos[i]
        result_rev.append(tree.query(ai))
        tree.update(ai, 1)

    result = result_rev[::-1]

    # output
    print(" ".join(str(x) for x in [case + 1] + result))
