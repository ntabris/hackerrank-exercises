def bincoef(n,k):
    r = 1;
    for x in range(n-k,n):
        #print("%f * %d" % (r,x+1))
        r = r * (x+1)
    for x in range(1,k):
        #print("%f / %d" % (r,x+1))
        r = r / (x+1.)
    return r

def pdf(n,k,p):
    r = (p**n) * ((1-p)**(k-n))
    return r

if __name__ == "__main__":


    b,g = map(float,input().split())
    p = b/(b+g)
    
    
    #print([ (pdf(i,6,p),bincoef(6,i),pdf(i,6,p)*bincoef(6,i)) for i in range(3,7) ])
    
    r = sum( pdf(i,6,p) * bincoef(6,i) for i in range(3,7) )
    print(round(r,3))