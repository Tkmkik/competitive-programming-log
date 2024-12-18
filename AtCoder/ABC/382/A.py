# https://atcoder.jp/contests/abc382/tasks/abc382_a AC

n, d = map(int, input().split())
s = input()

boxes = list(s)
# print("boxes: [" + " , ".join(boxes) + "]")

num_cookie = boxes.count("@")
eat_cookie = 0 if num_cookie <= d else num_cookie - d
# print("eat_cookie: " + str(eat_cookie))

result = n - eat_cookie
print(result)
