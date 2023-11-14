l = [14, 2, 29, 1, 3, 4]
x = 14
k = []
res = 0

# First loop
for i in range(1, 6):
    y = l.pop()
    if x != y:
        k.append(y)
    elif x == y:
        break

print(k)

# Second loop
for i in range(1, 6):
    # Check if k is empty before popping
    if not k:
        break

    y = k.pop()
    if y < x:
        res = y
        break
    elif y > x:
        # Remove the unnecessary pop here
        res = -1

print(res)
