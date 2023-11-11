'''
This is a solution to the problem - https://atcoder.jp/contests/abc328/tasks/abc328_f

The concept here is - weighted DSU. An indication for a problem to be related to this is multiple queries will be given of the type
a, b, d and we need to satisfy a condition X[a] - X[b] = d, for some sequence X.

We maintain an array w for storing the sum of weights of every node till their respective parents. The function find(a) returns the set leader
as well as the sum of weights for reaching the set leader. The combine(a, b, d) function assumes that set leaders of a and b are different, 
and consequently merges both the set maintaining the triangle law of addition.

Triangle Law:

A ------ B
 \     /
  \   /
   \ /
    C
Suppose the edges are A --> B (weight w1), B --> C (weight w2) and A --> C (weight w3), this implies w1 + w2 = w3.
'''

import sys, re
from collections import deque, defaultdict, Counter, OrderedDict
from itertools import permutations
from math import ceil, floor, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappush, heappop, heapify, nlargest, nsmallest
def STR(): return list(input())
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def list2d(a, b, c): return [[c] * b for i in range(a)]
def sortListWithIndex(listOfTuples, idx):   return (sorted(listOfTuples, key=lambda x: x[idx]))
def sortDictWithVal(passedDic):
    temp = sorted(passedDic.items(), key=lambda kv: (kv[1], kv[0]))
    toret = {}
    for tup in temp:
        toret[tup[0]] = tup[1]
    return toret
def sortDictWithKey(passedDic):
    return dict(OrderedDict(sorted(passedDic.items())))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 998244353

def find(x):
    cost = 0
    while(x!=rep[x]):
        cost += w[x]
        x = rep[x]
    return x, cost

def same(a, b):
    return find(a)[0] == find(b)[0]

def combine(a, b, d):
    a, cost_a = find(a)
    b, cost_b = find(b)

    if(a==b):
        return
    else:
        if(size[a]>size[b]):
            rep[b] = a
            w[b] = cost_a - (d + cost_b)
            size[a]+=size[b]
        else:
            rep[a] = b
            w[a] = d + cost_b - cost_a
            size[b]+=size[a]
    return

n,q = MAP()

ans = []

rep = list2d(n+1, 2, 0)

w = [0]*(n+1)

for i in range(1, n+1):
    rep[i] = i

size = [1]*(n+1)

for i in range(q):
    a,b,d = MAP()
    if(a==b):
        if(d==0):
            ans.append(i+1)
            continue
        else:
            continue

    if(same(a,b)):
        if(find(a)[1] - find(b)[1]== d):
            ans.append(i+1)
        else:
            continue
    else:
        combine(a,b,d)
        ans.append(i+1)

print(*ans)

