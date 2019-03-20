def bincoef(n,k):
    r = 1;
    for x in range(n-k,n):
        r = r * (x+1)
    for x in range(1,k):
        r = r / (x+1.)
    return r

def pdf(n,k,p):
    r = (p**n) * ((1-p)**(k-n))
    return r

if __name__ == "__main__":

    pp,batch = map(int,input().split())

    p = pp/100.     # p of reject
    p_bar = 1.-p     # p of good
    
    # p(no more than 2 rejects) = p(0 rej) + p(1 rej) + p(2 rej)
    r = sum(pdf(i,batch,p)*bincoef(batch,i) for i in range(3))
    print(round(r,3))
    
    # p(at least 2 rejects) = p(i rejects) from 2 to 10
    r = sum(pdf(i,batch,p)*bincoef(batch,i) for i in range(2,batch+1))
    print(round(r,3))