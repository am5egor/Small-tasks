c = int(input('введите целое трёхзначное число '))
e = c % 10
s = c // 100
a = c % 100 // 10
if s != a and a != e and s != e :
    print('все цыфры различны')
else :
    print('все цыфры одинаковы')