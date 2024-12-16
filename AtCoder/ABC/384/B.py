# https://atcoder.jp/contests/abc384/tasks/abc384_b AC


def is_div_1(div: int):
    if div == 1:
        return True
    elif div == 2:
        return False
    else:
        return ValueError(div)


def is_div1_rating(rating: int):
    if rating >= 1600 and rating <= 2799:
        return True
    else:
        return False


def is_div2_rating(rating: int):
    if rating >= 1200 and rating <= 2399:
        return True
    else:
        return False


if __name__ == "__main__":
    # variables
    n, r = map(int, input().split())
    d = []
    a = []

    # input
    for i in range(n):
        tmp1, tmp2 = map(int, input().split())
        d.append(tmp1)
        a.append(tmp2)

    # process
    for i in range(n):
        if is_div_1(d[i]):
            if is_div1_rating(r):
                r += a[i]
                continue
            else:
                continue
        else:
            if is_div2_rating(r):
                r += a[i]
                continue
            else:
                continue

    # output
    print(r)
