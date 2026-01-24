# f = open("/home/karel/Documents/ProgrameerOlympiade/opgaves/2012/cat3/morse/voorbeeld.invoer")


# def input():
#     return f.readline().strip()


def main():
    t = int(input())
    for _ in range(t):
        b, n = input().split(" ")
        n = int(n)

        p = b.count(".")
        l = b.count("-")

        for _ in range(n):
            p, l = p + 3 * l, p + l

        print(p + l)


if __name__ == '__main__':
    main()
