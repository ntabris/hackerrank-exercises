import math

if __name__ == "__main__":
    i, i_mu, i_sig = 100, 500, 80
    mu,sig = i*i_mu, (i**.5)*i_sig
    a = 250
    
#     cdf = lambda x: .5 * (1 + math.erf((x - mu)/(sig * 2**.5)))
#     print(round(cdf(a),4))
    
    mu,sig = 500,8

    a = mu - 1.96*sig
    b = mu + 1.96*sig

    print(round(a,2))
    print(round(b,2))


