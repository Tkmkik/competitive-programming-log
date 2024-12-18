# https://atcoder.jp/contests/abc383/tasks/abc383_a

n = int(input())
t = []
v = []
for i in range(n):
    t_i, v_i = map(int, input().split())
    t.append(t_i)
    v.append(v_i)

current_hour = 0
amount = 0

for i in range(n):
    # lost 1 L/water
    pass_hours = t[i] - current_hour
    amount -= pass_hours
    current_hour = t[i]
    # empty
    if amount < 0:
        amount = 0
    # add water
    amount += v[i]

print(amount)
