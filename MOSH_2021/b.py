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
for v in range (n):
    print(a[v])
b = copy.deepcopy(a)
a[0][1]='0'
for v in range (n):
    print(a[v])
otvet = [0]*k #массив для ответа
u = 0 # счетчик для массива ответа
sj = [0]*20
si = [0]*20
SJ = 0
SI = 0
q = 0 # счетчик для 1 элемента
i = 0 # координата
j = 0 # координата
d = 0 # счетчик
k1 = 0 # клон к1 для работы
m = 0 # счетчик массива с кодами
j1,i1 = 0,0 # пред.координаты
while k1 != k:
    while d == 0 and k1 != k:
        p = mas[m]
        
        if k1 % 2 == 0:
            while q == 0  and i<n:
                if a[j][i] == p:
                    q = 1
                    otvet[u] = (i+1)
                    a[j][i] = '0'
                    sj[SJ] = j
                    si[SI] = i
                    SJ += 1
                    SI += 1
                    u += 1
                    k1 += 1
                    m += 1
                if q != 1:
                    i += 1
            if i == n:
                a[sj[SJ-1]][si[SI-1]] = '-'
                d = 1
            else:
                
                q = 0
                j = 0
        else:
            while q == 0 and j < n:
                if a[j][i] == p:
                    q = 1
                    otvet[u] = j+1
                    a[j][i] = '0'
                    sj[SJ] = j
                    si[SI] = i
                    SJ += 1
                    SI += 1
                    u += 1
                    k1 += 1
                    m += 1
                if q != 1:
                    j += 1
            if j == n:
                a[sj[SJ-1]][si[SI-1]] = '-'
                d = 1
            else:
                
                q = 0
                i = 0
        
    if k1 == k:
        break
    u = u - 1
    otvet[u] = 0
    q = 0
    SI -= 1
    SJ -= 1
    j = sj[SJ]
    i = si[SI]
    sj[SJ] = 0
    si[SI] = 0
    k1 = k1 - 1
    m = m-1
    d = 0
    


print(' ')
print(otvet)
print(' ')
for v in range (n):
    print(a[v])



