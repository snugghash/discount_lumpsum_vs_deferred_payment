def f(x, y):
    return (x * 1.02) - y

if __name__=="__main__":
    p = 624
    y = p / 12
    x = p - y
    for i in range(12):
        x = f(x, y)
    print(x)

