### https://open.kattis.com/problems/justaminute
import sys

display = 0
real = 0

_count = -1 
for i in sys.stdin:
    if (_count < 0):
        _count = int(i)
    else:
        i = i.split()
        display += int(i[0])
        real += int(i[1])

display = (display * 60)

if real <= display:
    print('measurement error')
else:
    print(round(real / display,9))