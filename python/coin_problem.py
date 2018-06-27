import math
import os
import random
import re
import sys

def getResult(n, p):
    return search(n, sorted(list(set(p)), reverse=True), []) 

def search(n, p, visited):
    print("n: %d\tp: %s" % (n, p))
    myn = n
    if n in p:
        print("n in p")
        myn = 1
    elif n < min(p):
        print("%d < min(p): %d" % (n, min(p)))
        myn = -1
    else:
        try:
            subset = [m for m in p if m < n]
            print("subset: %s" % str(subset))
            for i in subset:
                if n-i not in visited:
                    total = 1 + search(n - i, subset, visited)
                    visited += [n - i]
                    if total <=0:
                        total = -1
                    elif total < myn:
                        myn = total
        except Exception as e:
            myn = -1
    return myn

result = getResult(1324, [4,5,6,7,8,9,10,1000,213])
print("FINAL RESULT: %d" % result)