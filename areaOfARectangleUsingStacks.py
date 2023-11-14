inp = [2, 1, 5, 6, 2, 3]
res = []
l = len(inp)
tot=[]
def fun(ele, ind):#left[] varuku traversal
    left = []
  
    for i in range(ind - 1, -1, -1):#Ee conditio emo (higherindex,smaller index)
        if inp[i] > ele:
            left.append(inp[i])
        else:
            break
    
    right = []
    for i in range(ind + 1, l):
        if inp[i] > ele:
            right.append(inp[i])
        else:
            break
    
    x = (len(left) + len(right)+1)#not includedbro thay element
    
    return x

for i in range(0, l):
    b = fun(inp[i], i)
    ar=(inp[i]*b)
    res.append(ar)

h = max(res)

print("Maximum value in res:", h)
