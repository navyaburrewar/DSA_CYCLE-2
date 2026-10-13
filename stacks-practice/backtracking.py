# given a number n- generate all strs of len n using only 'A' & 'B'


def generate(s, n):
    if len(s) == n:
        print(s)
        return

    generate(s + "A", n)
    generate(s + "B", n)


n = int(input("Enter n: "))
generate("", n)