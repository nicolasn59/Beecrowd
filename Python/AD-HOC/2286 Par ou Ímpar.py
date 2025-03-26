count = 1
while True:
    list = []
    n = int(input())

    if n == 0:
        break

    p1 = input().strip()
    p2 = input().strip()

    for i in range(n):
        a, b = map(int, input().split())
        list.append(p1 if (a + b) % 2 == 0 else p2)

    print(f'Teste {count}')
    for name in list:
        print(name)
    print()
    count += 1