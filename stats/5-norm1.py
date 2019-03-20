import math

if __name__ == "__main__":
    mu,sig = map(float,input().split())
    a = float(input())
    b,c = map(float,input().split())
    
    cdf = lambda x: .5 * (1 + math.erf((x - mu)/(sig * 2**.5)))
    
    print(round(cdf(a),3))
    print(round(cdf(c) - cdf(b),3))