import copy
f = open('qq.txt','r')
lines = f.readlines()
t = int(lines[0])
k = int(lines[2])
print(t,k)
mas = [str(y) for y in lines[3].split()]
print(mas)
n = int(lines[4])
print(n)
for i in range (n):
    a = [[str(x) for x in lines[i+5].split()] for i in range(n)]
b = copy.deepcopy(a)
a[1][3] = '--'
for v in range (n):
    print(a[v])
otvet = [0]*k

print('coppied')
for v in range (n):
    print(b[v])

k1 = 15
e = 0

kx = ['88','6','7','14','16','88']
if a[1][3] == '--':
    if b[1][3] == '32':
        for n in range(6):
            if kx[n] == str(k1):
                e = 1
                
                break
            else:
                print('8')
        if e == 0:
            print('sosi')

