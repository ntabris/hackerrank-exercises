import math

if __name__ == "__main__":
    mu,sig = map(float,input().split())
    a,b = float(input()),float(input())
    
    cdf = lambda x: .5 * (1 + math.erf((x - mu)/(sig * 2**.5)))
    
    print(round(100 - cdf(a)*100,2))
    print(round(100 - cdf(b)*100,2))
    print(round(cdf(b)*100,2))