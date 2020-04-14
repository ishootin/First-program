"""Алгоритм для проверки числа на простоту"""
from math import ceil, sqrt
from typing import Optional

def is_simple(n: int)-> Optional[bool]:
    if n == 1:
        return None
    for i in range (2, ceil(sqrt(n))+3):
        if n % i == 0:
            return False
    return True

n= int(input("Число для проверочки на простоту "))
print(is_simple(n))
