matrix = [
    [1, 2, 3, 4],
    [7, 8, 9, 10],
    [13, 14, 15, 16],
    [19, 20, 21, 22],
    [25, 26, 27, 28]
]


matrix = [
    [9718805, 60013003, 5103628, 85388216, 21884498, 38021292, 73470430, 31785927],
    [69999937, 71783860, 10329789, 96382322, 71055337, 30247265, 96087879, 93754371],
    [79943507, 75398396, 38446081, 34699742, 1408833, 51189, 17741775, 53195748],
    [79354991, 26629304, 86523163, 67042516, 54688734, 54630910, 6967117, 90198864],
    [84146680, 27762534, 6331115, 5932542, 29446517, 15654690, 92837327, 91644840],
    [58623600, 69622764, 2218936, 58592832, 49558405, 17112485, 38615864, 32720798],
    [49469904, 5270000, 32589026, 56425665, 23544383, 90502426, 63729346, 35319547],
    [20888810, 97945481, 85669747, 88915819, 96642353, 42430633, 47265349, 89653362],
    [55349226, 10844931, 25289229, 90786953, 22590518, 54702481, 71197978, 50410021],
    [9392211, 31297360, 27353496, 56239301, 7071172, 61983443, 86544343, 43779176]
]

matrix = [
[0, 0, 0, 0, 0, 0],
[0, 1, 1, 1, 1, 0],
[0, 1, 2, 2, 1, 0],
[0, 1, 2, 2, 1, 0],
[0, 1, 2, 2, 1, 0],
[0, 1, 1, 1, 1, 0],
[0, 0, 0, 0, 0, 0]
]

matrix = [
[1,2,3,4,5,6],
[2,8,9,10,11,7],
[3,7,6,5,4,8],
[4,5,6,7,8,9]
]

def listToMatrix(a):
    d = len(a) # "depth" of matrix
    h = len(a[0]['left']) + 2
    b = []

    # upper part
    for r in range(d):
        t = []
        for c in range(r):
            t.append( a[c]['left'][c-r] )
            #t.append( (c,c-r) )
        t.extend( a[r]['top'] )
        for c in range(r):
            t.append( a[r-c-1]['right'][c] )

        b.append(t)
    # mid part (no tops or bottoms)
    for rr in range(h-2*d):
        t = []
        r = rr + d

        fromBot = h - r - 1
        for c in range(d):
            t.append( a[c]['left'][fromBot-1-c] )
            #t.append( (c,fromBot-1-c) )

        for c in range(d):
            t.append( a[d-c-1]['right'][c+rr] )
            #t.append( (d-c-1, c+rr) )

        b.append(t)
    # lower part
    for r in range(d):
        t = []

        fromBot = d-r-1
        #t.append( fromBot )
        for c in range(fromBot):
            t.append( a[c]['left'][fromBot - c - 1])
            #t.append( (c, fromBot - c - 1) )

        t.extend( a[d-r-1]['bot'][::-1] )

        for c in range(fromBot):
            t.append( a[fromBot-c-1]['right'][-1-c] )
            #t.append( (fromBot - c - 1, -1-c) )

        b.append(t)

    return b

[i for i in range(3,-1,-1)]
def matrixToList(matrix):
    m = len(matrix) # rows
    n = len(matrix[0]) # cols
    cycles = int(min(m,n)/2) # how many nested cycles
    result = []
    for i in range(cycles):
        s = dict()
        myRows = m - (i*2)
        myCols = n - (i*2)

        s['top'] = matrix[i][i:i+myCols]
        s['right'] = [ matrix[i + j][i+myCols-1] for j in range(1,myRows-1) ]
        s['bot'] = matrix[i + myRows - 1][i:i+myCols][::-1]
        s['left'] = [ matrix[i + j][i] for j in range(1,myRows-1) ][::-1]

        result.append(s)
    return(result)

def printMatrix(a):
    for r in a:
        print(*r)

def rotateMatrix(a,n):
    for i in range(len(a)):
        w = len(a[i]['top'])
        h = len(a[i]['left'])
        s = a[i]['top'] + a[i]['right'] + a[i]['bot'] + a[i]['left']
        m = len(s)
        z = s[n%m:] + s[:n%m]
        a[i]['top'] = z[:w]
        a[i]['right'] = z[w:w+h]
        a[i]['bot'] = z[w+h:w+w+h]
        a[i]['left'] = z[w+w+h:w+w+h+h]


printMatrix(matrix)
a = matrixToList(matrix)

rotateMatrix(a,40)
#a[0]['top']
# 1 from bot, get 1, from left(0,0)
b = listToMatrix(a)
printMatrix(b)
