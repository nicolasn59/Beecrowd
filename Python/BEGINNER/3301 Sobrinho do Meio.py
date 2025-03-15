h, z, l = map(int, input().split())
if z < h < l or l < h < z:
    print("huguinho")
elif h < z < l or l < z < h:
    print("zezinho")
else:
    print("luisinho")
