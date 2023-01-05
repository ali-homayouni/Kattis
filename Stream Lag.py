### https://open.kattis.com/problems/streamlag

import sys

_count = -1

lag = 0
for d in sys.stdin:
    if (_count < 0):
        _count = int(d)
    else:
        d = d.split()
        ti = int(d[0])
        i = int(d[1])
        dif = ti - i
        if dif > lag:
            lag += dif - lag

print(lag)