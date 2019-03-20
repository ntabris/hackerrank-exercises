if __name__ == "__main__":
    x,y = map(float,input().split())
    
    ca = 160 + 40*(x + x**2)
    cb = 128 + 40*(y + y**2)
    
    print(round(ca,3))
    print(round(cb,3))