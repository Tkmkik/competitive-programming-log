# https://atcoder.jp/contests/abc384/tasks/abc384_a AC

if __name__ == "__main__":
    n_str, c1, c2 = input().split()
    s = input()

    ans = ""

    for s_i in s:
        if s_i is c1:
            next = c1
        else:
            next = c2
        ans += next

    print(ans)
