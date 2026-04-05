#23
#def f(a,b):
#    if a == b:
#        return 1
#    if a>b:
#        return 0
#    return f(a+2,b)+f(a*4,b)
#print(f(3,200)*f(200,510))

#25
#def prime(x):
#    count = 0
#    for i in range(2, int(x ** 0.5)+1):
#        if x % i == 0:
#            count += 1 
#            if x // i != i:
#                count += 1 
#    if count != 0:
#        return False
#    else:
#        return True
#for N in range(7430068, 7430268):
#    a = []
#    for i in range(2, int(N ** 0.5)+1):
#        if N % i == 0:
#            if prime(i):
#                a.append(i)
#            if N // i != i:
#                if prime(N // i):
#                    a.append(N // i)
#    if len(a) != 0:
#        M = max(a) + min(a)
#        if M % 29 == 11:
#            print(N, M)

#2
#print('x','y', 'z','w')
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            for w in range(2):
#                if ((not((w or x))<=z and (not(x==y))))==1:
#                    print(x,y,z,w)

#19-21
#def f(s, m):
#    if s <= 10:
#        return m % 2 == 0
#    if m == 0:
#        return 0
#    h = [f(s - 1  , m - 1), f(s - 3 , m - 1), f(s //2  , m - 1)]
#    return any(h) if (m - 1) % 2 == 0 else all(h)
#print('19', [s for s in range(11, 1000) if f(s, 2)])
#print('20', [s for s in range(11, 1000) if not f(s, 1) and f(s, 3)])
#print('21', [s for s in range(11, 1000) if not f(s, 2) and f(s, 4)])
