# Closing: closes one and opens two tabs
# Clicked: Closes one tab
initial, actions = map(int, input().split())
for _ in range(actions):
    tabs = input()
    if tabs == 'fechou':
        initial += 1
    else:
        initial -= 1
print(initial)