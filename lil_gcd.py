"""Опять пайлинт ругается"""
def gcd(n_1, n_2):
    """Вот, больше не ругается"""
    return n_1 if n_2 == 0 else gcd(n_2, n_1 % n_2)
a: int = int(input("Число номер один"+'\n'))
b: int = int(input("Число номер два"+'\n'))
print(gcd(a, b))
