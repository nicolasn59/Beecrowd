distance = 0
intervals = int(input())
for _ in range(intervals):
    hours, averageSpeed = map(int, input().split())
    distance += hours * averageSpeed
print(distance)