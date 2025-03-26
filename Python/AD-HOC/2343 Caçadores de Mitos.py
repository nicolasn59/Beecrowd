def repeatedRays(records):
    quadrantSet = set()  # SET DOES NOT ALLOW DUPLICATE ELEMENTS
    for ray in records:
        quadrant = f"{ray[0]}_{ray[1]}" # CONCATENATING VALUES INTO A SINGLE STRING REDUCES EXECUTION TIME BY HALF
        if quadrant in quadrantSet:
            return 1
        quadrantSet.add(quadrant)
    return 0


records = []
n = int(input())

for _ in range(n):
    x, y = list(map(int, input().split()))
    records.append((x, y))

print(repeatedRays(records))