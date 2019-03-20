s = []
s.append([2, 9, 8])
s.append([4, 2 ,7])
s.append([5, 6 ,7])

magic = []
import itertools
pp = itertools.permutations(range(1,10))
for p in pp:
    if isMagic(p):
        magic.append(list(p))

ss = list(itertools.chain(*s))

costs = []
for i in range(0,len(magic)):
    costs.append( cost(magic[i], ss) )

print(min(costs))


def isMagic(p,n = 3):
    mk = n * (n**2 + 1) / 2
    rows = all(sum(p[n*i:n*(i+1)]) == mk for i in range(0,n))
    cols = all(sum(p[i::n]) == mk for i in range(0,n))
    lr = sum(p[n * i + i] for i in range(0,n)) == 15
    rl = sum(p[n*i-i] for i in range(1,n+1)) == 15
    return rows and cols and lr and rl

def cost(a,b):
    return sum(abs(a[i] - b[i]) for i in range(0,len(a)))
    
