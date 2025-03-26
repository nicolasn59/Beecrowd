# SUBPROGRAM
def partition(balls, left, right):
    pivot = balls[right]
    i = left - 1
    for j in range(left, right):
        if balls[j] <= pivot:
            i = i+1
            balls[i], balls[j] = balls[j], balls[i]
    balls[i+1], balls[right] = balls[right], balls[i+1]
    return i+1

def quicksort(balls, left, right):
    if left < right:
        pivot = partition(balls, left, right)
        quicksort(balls, left, pivot-1)
        quicksort(balls, pivot+1, right)
    return balls

def draw(comb, numBalls):
    balls = list(map(int, input().split()))
    balls = quicksort(balls, 0, (len(balls)-1))
    numCombs = list()
    numCombs += [0]
    while len(balls) != 0:
        for j in range(0, len(balls)):
            num = abs(balls[0] - balls[j])
            if num <= comb:
                if num not in numCombs:
                    numCombs += [num]
            if len(numCombs) == (comb+1):
                print("Y")
                return None
        if len(numCombs) == (comb+1):
            print("Y")
            return None
        balls.pop(0)
    if len(numCombs) == (comb+1):
        print("Y")
        return None
    else:
        print("N")
        return None

# MAIN
combination, numBalls = map(int, input().split())
while combination != 0 or numBalls != 0:
    draw(combination, numBalls)
    combination, numBalls = map(int, input().split())