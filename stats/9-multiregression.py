import numpy as np
import numpy.linalg as linalg

m,n = map(int,input().split())
x = []
y = []
for i in range(n):
    a = [1]
    *xi,yi = map(float,input().split())
    a.extend(xi)
    x.append(a)
    y.append(yi)
    
    
q = int(input())
fit = []
for i in range(q):
    a = [1]
    xi = map(float,input().split())
    a.extend(xi)
    fit.append(a)


#x = [[1, 5, 7], [1, 6, 6], [1, 7, 4], [1, 8, 5], [1, 9, 6]]
#y = [10, 20, 60, 40, 50]

X = np.asarray(x)
Y = np.asarray(y)

XT = X.transpose()
XTX = np.dot(XT,X)
XTXinv = linalg.inv(XTX)
B = linalg.multi_dot([XTXinv,XT,Y])

predict = np.dot(fit,B)
for i in predict:
    print(round(i,2))