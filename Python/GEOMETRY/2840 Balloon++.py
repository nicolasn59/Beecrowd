radius, liters = map(int, input().split())
volume = (4 * 3.1415 * (radius**3)) / 3
print(int(liters // volume))