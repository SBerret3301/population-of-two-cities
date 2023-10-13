x = 500000
y = 1000000
i = 0
while x < y :
    i = i + 1
    x = x + x * 0.08
    y = y + y * 0.05
print(i)
