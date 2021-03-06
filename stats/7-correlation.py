def stat_params(a):
    mu = sum(a)/len(a)
    rss = sum( (x-mu)**2 for x in a )
    return mu,(rss/len(a))**.5

def corr(a,b):
    a_mu,a_sig = stat_params(a)
    b_mu,b_sig = stat_params(b)
    
    cov = sum( (a[i]-a_mu)*(b[i]-b_mu) for i in range(len(a)) )/len(a)
    
    return cov/(a_sig*b_sig)

def rank(a):
    values = sorted(set(a))
    ranks = [ values.index(x)+1 for x in a ]
    return ranks

def spearman(a,b):
    return corr(rank(a),rank(b))

if __name__ == "__main__":
    n = int(input())
    x = list(map(float,input().split()))
    y = list(map(float,input().split()))
    
    print(round(spearman(x,y),3))