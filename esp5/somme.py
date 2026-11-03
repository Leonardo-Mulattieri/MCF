import os

def sum_prod(n):
    c = 0
    k = 1
    for i in range(1,n+1):
        k = k*i
        print(k)
    
    for i in range(n+1):
        c = c + i
        
    return c,k

def rad_pow(n, e, a = 1):
    c = 0
    k = 0
    for i in range(n+1):
        c = c + i**(1/e)

    for i in range(n+1):
        k = k + i**a

    return c , k



os.system('ls /usr');
