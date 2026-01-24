from copy import deepcopy


# f = open("/home/karel/Documents/ProgrameerOlympiade/opgaves/2012/cat3/hercules/voorbeeld.invoer")


# def input():
#     return f.readline().strip()


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())

        map = {}

        for _ in range(n):
            parent, _, *children = input().split()
            map[parent] = children

        def f(n):
            if n == "*":
                return []
            return [f(c) for c in map[n]]

        root = f("stam")

        def cut(n):
            assert n
            if n[-1] == []:
                n.pop()
            else:
                cut(n[-1])

        c = 0
        while root != []:
            c += 1
            if root[-1] == []:
                root.pop()
            else:
                cut(root[-1])
                root.append(deepcopy(root[-1]))

        print(c)

    # print(t)


if __name__ == '__main__':
    main()
