# f = open("/home/karel/Documents/ProgrameerOlympiade/opgaves/2012/cat3/woordsnippers/voorbeeld.invoer")
#
#
# def input():
#     return f.readline().strip()


def main():
    t = int(input())
    for _ in range(t):
        pieces = input().split(" ")

        k = len(pieces[0])
        n = len(pieces) + k - 1

        def f(s: str, used: int):
            if used == 2 ** len(pieces) - 1:
                print(s)
                return True

            for i in range(len(pieces)):
                if used & (1 << i):
                    continue
                p = pieces[i]
                if s[-k + 1:] == p[:-1]:
                    if f(s + p[-1], used | (1 << i)):
                        return True

            return False

        for j in range(len(pieces)):
            if f(pieces[j], 1 << j):
                break


if __name__ == '__main__':
    main()
