def f(x, y, rate = 1.04):
    return (x * rate) - y



def findReturn(p, y, rate = 1.04, t = 11):
    x = p - y
    for i in range(t):
        x = f(x, y, rate) # Careful of mutable elements
    return x



if __name__=="__main__":
    # Discounted lumpsum price
    p = 535
    # Credited, payment over a period of time
    t = 12
    price_when_delaying_payment = 654
    y = price_when_delaying_payment / (t)
    maxReturn = 0
    for r in range(50):
        rate = r/100 + 1
        tmp = findReturn(p, y, rate, t-1)
        print(tmp)
        if (tmp > maxReturn):
            maxReturn = tmp
            maxRate = rate
    print(maxReturn, maxRate)

