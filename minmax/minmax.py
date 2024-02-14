def next_int() -> int:
    return int(input().strip())

nr_lists = next_int()

for i in range(int(nr_lists)):
    nr_ints = int(next_int())
    lst_ints = []
    for _ in range(nr_ints):
        lst_ints.append(next_int())
    print(f"{i+1} {min(lst_ints)} {max(lst_ints)}", end = "\n")