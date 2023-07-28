num[10] = {3,4,6,2,1,6,8,2,9,5}
x = 2
y = 3
num[x] = num[x * y]
num[num[x]] = num[x + y]
num[y+1] = x + y
num[y-x] = num[num[y]]
num[y] = num[y] + num[x]
num[x-2] = num[y] + x

for(i = 1, i = 11, i++):
    print(num[i])
