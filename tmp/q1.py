
import time
from itertools import combinations, product
import numpy as np


def check(data1, data2):
    _l = len(data1)
    count = 0
    cini1 = 1
    cini2 = 1
    empty1 = set()
    empty2 = set()
    # print(data1)
    while len(empty1) < _l and len(empty2) < _l:
        for row in range(_l):
            data1[row].discard(cini1)
            data2[row].discard(cini2)
            if len(data1[row]) == 0:
                empty1.add(row)
            if len(data2[row]) == 0:
                empty2.add(row)

            cini1 = (cini1 % _l) + 1
            cini2 = (cini2 % _l) + 1
        count += 1
        cini1 = (cini1 % _l) + 1
        cini2 = ((cini2 % _l) + 1) % _l + 1
        print(data1, data2)
    count -= 1
    return count


def check2(data1, data2):
    _l = len(data1)
    count = -1

    empty1 = set()
    empty2 = set()
    index = 1

    while index <= _l:
        cini1 = cini2 = index
        for row in range(_l):
            data1[row].discard(cini1)
            data2[row].discard(cini2)
            cini1 = (cini1 % _l) + 1
            cini2 = ((cini2 % _l) + 1) % _l + 1
            if len(data1[row]) == 0:
                empty1.add(row)
                if len(empty1) == _l:
                    index = _l + 1
                    break
            if len(data2[row]) == 0:
                empty2.add(row)
                if len(empty2) == _l:
                    index = _l + 1
                    break
        # if index < _l:
        # print(data1,data2)
        count += 1
        index += 1
        # cini1 = (cini1 % _l) + 1
        # cini2 = ((cini2 % _l) + 1) % _l + 1

    return count


def check3(data1, data2):
    _l = len(data1)
    d1 = list(range(1, _l+1))
    d2 = list(range(1, _l+1))
    em1 = set()
    em2 = set()

    for i in range(_l):
        for j in range(len(d1)):
            data1[j].discard(d1[j])
            data2[j].discard(d2[j])
            if len(data1[j]) == 0:
                em1.add(j)
            if len(data2[j]) == 0:
                em2.add(j)
        if len(em1) == _l or len(em2) == _l:
            return i
        d1 = d1[1:] + d1[:1]
        d2 = d2[-1:] + d2[:-1]
    print(i, d1, d2)
    print('-------------------------------------------------------------------------------')


def binarySearch(v, To_Find):
    lo = 0
    hi = len(v) - 1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if v[mid] < To_Find:
            lo = mid + 1
        else:
            hi = mid
    if v[lo] >= To_Find:
        return v[:lo], v[lo:]
    elif v[hi] >= To_Find:
        return v[:hi], v[hi:]
    else:
        return v, []


def check4(data1):
    _len = len(data1)
    jelo_max = 0
    aghab_max = 0

    for index, v in enumerate(data1):
        v = list(v)
        index += 1
        if len(v) == 0:
            continue

        jelo = 0
        aghab = 0
        
        lo = 0
        hi = len(v) - 1
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if v[mid] < index:
                lo = mid + 1
            else:
                hi = mid
        if v[lo] >= index:
            l1 = v[:lo]
            l2 = v[lo:]
        elif v[hi] >= index:
            l1 =  v[:hi]
            l2 = v[hi:]
        else:
            l1 = v
            l2 = []
        
        lenl1 = len(l1)
        lenl2 = len(l2)

        if lenl1 != 0:
            jelo = _len - (index - l1[lenl1-1])
        else:
            jelo = l2[lenl2-1] - index

        if lenl2 != 0:
            aghab = _len - (l2[0] - index)
        else:
            aghab = index - l1[0]

        jelo_max = max(jelo_max, jelo)
        aghab_max = max(aghab_max, aghab)

    return min(jelo_max, aghab_max)



def check5(data1):
    _len = len(data1)
    jelo_max = 0
    aghab_max = 0

    for index, v in enumerate(data1):
        v = list(v)
        index += 1
        if len(v) == 0:
            continue
        _str = str(index)+str(v)
        if _str in _cache:
            jelo = _cache[_str]['jelo']
            aghab = _cache[_str]['aghab']
        else:
            jelo = 0
            aghab = 0

            lo = 0
            hi = len(v) - 1
            while hi - lo > 1:
                mid = (hi + lo) // 2
                if v[mid] < index:
                    lo = mid + 1
                else:
                    hi = mid
            if v[lo] >= index:
                l1 = v[:lo]
                l2 = v[lo:]
            elif v[hi] >= index:
                l1 =  v[:hi]
                l2 = v[hi:]
            else:
                l1 = v
                l2 = []
                
            lenl1 = len(l1)
            lenl2 = len(l2)

            if lenl1 != 0:
                jelo = _len - (index - l1[lenl1-1])
            else:
                jelo = l2[lenl2-1] - index

            if lenl2 != 0:
                aghab = _len - (l2[0] - index)
            else:
                aghab = index - l1[0]
            _cache[_str] = {'jelo': jelo, 'aghab': aghab}
        
        if jelo > jelo_max:
            jelo_max = jelo
        if aghab > aghab_max:
            aghab_max = aghab
    if jelo_max <= aghab_max:
        return jelo_max
    return aghab_max   

def check6(index, v, _len):
    _str = str(v)
    v.discard(index)
    v = list(v)    
    if len(v) == 0:
        _cache['jelo'][index].append(0)
        _cache['aghab'][index].append(0)
        return

    jelo = 0
    aghab = 0

    lo = 0
    hi = len(v) - 1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if v[mid] < index:
            lo = mid + 1
        else:
            hi = mid
    if v[lo] >= index:
        l1 = v[:lo]
        l2 = v[lo:]
    elif v[hi] >= index:
        l1 =  v[:hi]
        l2 = v[hi:]
    else:
        l1 = v
        l2 = []
        
    lenl1 = len(l1)
    lenl2 = len(l2)

    if lenl1 != 0:
        jelo = _len - (index - l1[lenl1-1])
    else:
        jelo = l2[lenl2-1] - index

    if lenl2 != 0:
        aghab = _len - (l2[0] - index)
    else:
        aghab = index - l1[0]

    _cache['jelo'][index].append(jelo)
    _cache['aghab'][index].append(aghab)


with open(r'C:\Users\494807\Desktop\Projects\jessica\24583b9b41590c44\justaminute.02.in', 'r') as f:
    red = f.readlines()

_cache = {'jelo':{},'aghab':{}}
_count = -1
data = []
CC = 1
for i in red:
    if (_count < 0):
        _count = int(i)
    else:
        
        i = i.split()
        if len(i) == 1:
            CC += 1
            continue
        _cache['jelo'][CC] = [0]
        _cache['aghab'][CC] = [0]
        item = list(set([int(j) for j in i[1:]]))            
        
        li = [{}]
        for r in range(1,len(item)+1):
            for l in list(combinations(item, r)):
                l = set(l)
                # l.discard(CC)
                li.append(l)
                check6(CC,l,_count)
        data.append(li)
        CC += 1

print(_cache,'\n')
jelo_s = [np.array(set(item)) for item in list(_cache['jelo'].values())]
aghab_s = [np.array(set(item)) for item in list(_cache['aghab'].values())]

# print(jelo,'\n')
# print(aghab,'\n')

# print([max(list(i)) for i in list(product(*jelo))],'\n')
# print([max(list(i)) for i in list(product(*aghab))],'\n')

jelo_s = np.array(list(product(*jelo_s)))
aghab_s = np.array(list(product(*aghab_s)))

# jelo = jelo.max(axis=1)
# aghab = aghab.max(axis=1)

# jelo = [max(list(i)) for i in list(product(*jelo))]
# aghab = [max(list(i)) for i in list(product(*aghab))]

jelo = np.array(jelo.max(axis=1)).reshape(1,jelo.shape[0])
aghab = np.array(aghab.max(axis=1)).reshape(1,aghab.shape[0])



c = np.sum(np.concatenate([jelo,aghab]).min(axis=0))
# for i in range(len(aghab)):
#     c += min(jelo[i],aghab[i])
print(c)
exit()
data = [list(i) for i in list(product(*data))]
c = 0
_cache = {i:{} for i in range(1,len(data[0])+1)}
for dish in data:
    c += check5(dish)

print(c)
# print(_cache)
# un = set()
# for i in _cache:
#     un.update(set(_cache[i]))
# # print(un)
# _oiu=0
# for u in un:
#     for i in _cache:
#         if u in _cache[i]:
#             print(u, i, _cache[i][u])
#             _oiu+=1
#     print('---------')



from itertools import combinations, product
import sys

_cache = {}
def check(data1):
    _len = len(data1)
    jelo_max = 0
    aghab_max = 0

    for index, v in enumerate(data1):
        v = list(v)
        index += 1
        if len(v) == 0:
            continue
        _str = str(index)+str(v)
        if _str in _cache:
            jelo = _cache[_str]['jelo']
            aghab = _cache[_str]['aghab']
        else:
            jelo = 0
            aghab = 0

            lo = 0
            hi = len(v) - 1
            while hi - lo > 1:
                mid = (hi + lo) // 2
                if v[mid] < index:
                    lo = mid + 1
                else:
                    hi = mid
            if v[lo] >= index:
                l1 = v[:lo]
                l2 = v[lo:]
            elif v[hi] >= index:
                l1 =  v[:hi]
                l2 = v[hi:]
            else:
                l1 = v
                l2 = []
                
            lenl1 = len(l1)
            lenl2 = len(l2)

            if lenl1 != 0:
                jelo = _len - (index - l1[lenl1-1])
            else:
                jelo = l2[lenl2-1] - index

            if lenl2 != 0:
                aghab = _len - (l2[0] - index)
            else:
                aghab = index - l1[0]
            _cache[_str] = {'jelo': jelo, 'aghab': aghab}
        
        if jelo > jelo_max:
            jelo_max = jelo
        if aghab > aghab_max:
            aghab_max = aghab
    if jelo_max <= aghab_max:
        return jelo_max
    return aghab_max    
    
    
_count = -1
data = []
CC = 1
for i in sys.stdin:
    if (_count < 0):
        _count = int(i)
    else:
        i = i.split()
        item = [int(j) for j in set(i[1:])]
        li = []
        for r in range(len(item)+1):
            for l in list(combinations(item, r)):
                l = set(l)
                l.discard(CC)
                li.append(l)
        data.append(li)
        CC += 1
        
data = [list(i) for i in list(product(*data))]

c = 0
for dish in data:
    c += check(dish)
print(c)



from itertools import combinations, product
import sys

_cache = {'jelo':{},'aghab':{}}
def check(index, v, _len):
    _str = str(v)
    v.discard(index)
    v = list(v)    
    if len(v) == 0:
        _cache['jelo'][index].append(0)
        _cache['aghab'][index].append(0)
        return

    jelo = 0
    aghab = 0

    lo = 0
    hi = len(v) - 1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        if v[mid] < index:
            lo = mid + 1
        else:
            hi = mid
    if v[lo] >= index:
        l1 = v[:lo]
        l2 = v[lo:]
    elif v[hi] >= index:
        l1 =  v[:hi]
        l2 = v[hi:]
    else:
        l1 = v
        l2 = []
        
    lenl1 = len(l1)
    lenl2 = len(l2)

    if lenl1 != 0:
        jelo = _len - (index - l1[lenl1-1])
    else:
        jelo = l2[lenl2-1] - index

    if lenl2 != 0:
        aghab = _len - (l2[0] - index)
    else:
        aghab = index - l1[0]

    _cache['jelo'][index].append(jelo)
    _cache['aghab'][index].append(aghab)
    
_count = -1
data = []
CC = 1
for i in sys.stdin:
    if (_count < 0):
        _count = int(i)
    else:
        
        i = i.split()
        if len(i) == 1:
            CC += 1
            continue
        _cache['jelo'][CC] = [0]
        _cache['aghab'][CC] = [0]
        item = set([int(j) for j in i[1:]])
        
        li = [{}]
        for r in range(1,len(item)+1):
            for l in list(combinations(item, r)):
                l = set(l)
                # l.discard(CC)
                li.append(l)
                check(CC,l,_count)
        data.append(li)
        CC += 1

jelo = list(_cache['jelo'].values())
aghab = list(_cache['aghab'].values())

jelo = [max(list(i)) for i in list(product(*jelo))]
aghab = [max(list(i)) for i in list(product(*aghab))]
c = 0
for i in range(len(jelo)):
    c+= min(jelo[i],aghab[i])
print(c)
