from itertools import combinations
import numpy as np
from math import pow

with open(r'C:\Users\494807\Desktop\Projects\jessica\24583b9b41590c44\justaminute.02.in', 'r') as f:
    red = f.readlines()

_count = -1
_l = []
po = 1
for i in red:

    if (_count < 0):
        _count = int(i)
        # po = int(pow(2, _count))
    else:
        i = i.split()
        item = i[1:]
        li = np.zeros((1, 1, _count))
        for r in range(1, len(item)+1):
            _combinations = list(combinations(item, r))
            
            # print(item, _combinations)
            for combination in _combinations:
                item_list = np.zeros((1, 1, _count))
                for com in combination:
                    item_list[0][0][int(com)-1] = 1
                li = np.concatenate([li, item_list], axis=1).reshape(
                    1, li.shape[1]+1, 3)
        po *= li.shape[1]
        
        _l.append(li)

    
# li = np.concatenate(_l, axis=-1)

# print(li.shape)
# li = li.reshape(po,_count,_count)
# print(li)
# print(li.shape)

for i, l in enumerate(_l):
    print(l,'\n', l.shape)    
    _l[i] = np.repeat(l, int(po/l.shape[1]), axis=0).reshape(1, po, _count)
    print(_l[i],'\n', _l[i].shape)    
    break
# for l in _l:
#     print(l)  
# print(_l) 


