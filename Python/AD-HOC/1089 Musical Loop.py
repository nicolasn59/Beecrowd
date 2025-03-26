while True:
    n = int(input())

    if n == 0:
        break

    h = list(map(int, input().split()))
    h.append(h[0])
    h.insert(0, h[-2])

    peak = 0

    for i in range(1, (len(h))):
        if (i + 1) < len(h):
            if h[i-1] > h[i] < h[i+1]: # H1 AT MINIMUM PEAK (HIGHER - LOWER - HIGHER)
                peak += 1
            else:
                if h[i-1] < h[i] > h[i+1]: # H1 AT MAXIMUM PEAK (LOWER - HIGHER - LOWER)
                    peak += 1
    print(peak)