adj = [
'YYNNN',
'YYYNN',
'NNYNN',
'NNNYY',
'NNNNY'
]

matrix = [ [c == 'Y' for c in r] for r in adj ]

starts = set(range(len(matrix)))
circles = []

while len(starts) > 0:
    before = {starts.pop()}
    while True:
        after = expand(before)
        diff = after.difference(before)
        before = after
        if len(diff) == 0:
            break
    circles.append(after)
    starts = starts.difference(after)

print(circles)



def expand(nodes):
    expansion = set()
    for node in nodes:
        expansion = expansion.union( i for i in range(len(matrix[0])) if matrix[node][i]  )
    nodes = nodes.union(expansion)
    return nodes
