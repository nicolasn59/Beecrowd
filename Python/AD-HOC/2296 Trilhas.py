def calculate_effort(altitude):
    effort = 0
    for i in range(1, len(altitude)):
        elevation = altitude[i] - altitude[i -1]
        if elevation > 0:
            effort += elevation
    return effort


def find_easy_trail(trails):
    min_effort = float('inf')
    best_trail = -1

    for index, altitude in enumerate(trails):
        effort = min(calculate_effort(altitude), calculate_effort(altitude[::-1]))
        if effort < min_effort:
            min_effort = effort
            best_trail = index + 1
    return best_trail


num_tests = int(input())
trails = []
for _ in range(num_tests):
    altitudes = list(map(int, input().split()))[1:]
    trails.append(altitudes)

print(find_easy_trail(trails))