### https://open.kattis.com/problems/dimsum


### Solution 1:

def s1():
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


def s2():
    from itertools import combinations, product
    import sys
    import numpy as np

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
        

    _cache = {'jelo':{},'aghab':{}}
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
                    check6(CC,l,_count)
            data.append(li)
            CC += 1

    jelo = [np.array(item) for item in list(_cache['jelo'].values())]
    aghab = [np.array(item) for item in list(_cache['aghab'].values())]

    jelo = np.array(list(product(*jelo)))
    aghab = np.array(list(product(*aghab)))

    jelo = np.array(jelo.max(axis=1)).reshape(1,jelo.shape[0])
    aghab = np.array(aghab.max(axis=1)).reshape(1,aghab.shape[0])


    c = np.sum(np.concatenate([jelo,aghab]).min(axis=0))
    print(c)


def s3():
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