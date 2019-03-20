import math

def pois(k,l):
    return (l**k) * (math.e**(-l)) / math.factorial(k)

if __name__ == "__main__":
    l = float(input())
    k = float(input())
    
    print(round(pois(k,l),3))