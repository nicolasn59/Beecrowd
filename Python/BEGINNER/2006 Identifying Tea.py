teaType = int(input())
a, b, c, d, e = map(int, input().split())
count = 0
if a == teaType:
    count += 1
if b == teaType:
    count += 1
if c == teaType:
    count += 1
if d == teaType:
    count += 1
if e == teaType:
    count += 1
print(count)