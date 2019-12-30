"""Перевод числа в любую систему исчисления, но до 36"""

def int_to_str(n):
    if n<10 and n>=0:
        return chr(n+ord("0"))
    else:
        return chr(n-10+ord("A"))
    
def func_perevod(x:int, base:int):
    str=""
    while x != 0:
        rest= x % base
        str+= int_to_str(rest)
        x //= base
    return ''.join(reversed(str))
x= int(input("Число для перевода "+'\n'))
base= int(input("В какой системе счисления (до 36)"+'\n'))
print(func_perevod(x, base))
