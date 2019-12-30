"""Алгоритм подсчета крутого gcd и коэффициентов Безу"""

def lil_gcd(a, b):
    return a if b == 0 else lil_gcd(b, a % b)

def gcd(a,b):
    if (a==b):
        return (a, 1, 0)
    a1 = int(a/lil_gcd(a,b))
    b1 = int(b/lil_gcd(a,b))
    if (a1 > b1):
        a1 , b1 = b1, a1
    k = int(b1)
    u = 1
    for i in range (1, k):
        if (u*a1 % b1 == 1):
            v = int((1-u*a1)/b1)
            return(lil_gcd(a,b),v,u)
        else: u=u+1
    return (lil_gcd(a, b), )      
a: int = int(input("Число номер один"+'\n'))
b: int = int(input("Число номер два"+'\n'))

print(gcd(a,b))
