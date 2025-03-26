inside = outside = 0
inputs = int(input())
for i in range(1, inputs + 1):
    value = int(input())
    if 10 <= value <= 20:
        inside += 1
    else:
        outside += 1
print("%d in" % inside)
print("%d out" % outside)
