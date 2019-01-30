#!E:/Tools/Python


"""
def frange(start, stop, step):
     i = start
     while i < stop:
         yield i
         i += step

for i in frange(0.5, 1.0, 0.1):
    print(i)
"""
"""
for i in range(99, 0, -1):
        if i == 1:
                print('1 bottle of beer on the wall, 1 bottle of beer!')
                print('So take it down, pass it around, no more bottles of beer on the wall!')
        elif i == 2:
                print('2 more bottles of beer on the wall, 2 more bottles of beer!')
                print('So take one down, pass it around, 1 more bottle of beer on the wall!')
        else:
                print('{0} bottles of beer on the wall, {0} bottles of beer!'.format(i))
                print('So take it down, pass it around, {0} more bottles of beer on the wall!'.format(i - 1))
"""
"""
a = {}
for x in range(1,5):
    a[x] = x**2


b = []

for x in range(1,5):
    b.append(x**2)
"""
"""
P = 20
n = 1
for x in range(1, P+1):
    exec("A{} = n".format(x))
    n = n+1
"""
