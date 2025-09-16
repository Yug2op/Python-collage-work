n = 42
k = 4
mask = (n >> k) & 1
if mask:
    print("Set")
else:
    print("Not Set")