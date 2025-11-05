import random
def preSorted(n):
    return list(range(n))

def mostlySorted(n):
    x = preSorted(n) 
    y = n//10 + 1
    indices = []
    for i in range(0, y):
        indices.append(random.randint(0, n-1))
        a = random.randint(0, n-1)
        b = random.randint(0, n-1)
        x[a], x[b] = x[b], x[a]
    return x

def reversed(n):
    return list(range(n-1, -1, -1))

def randomList(n):
    x = list(range(n))
    random.shuffle(x)
    return x


