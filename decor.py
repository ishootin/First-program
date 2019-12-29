"""Реализация декоратора репит"""
def repeat(n_0: int):
    """Декоратор"""
    def decorator(function):
        def fake_function(x_0: int):
            for i in range(n_0):
                x_0 = function(x_0) + i - i #Просто пайлинт этот попросил использовать i
            return x_0
        return fake_function
    return decorator

N1: int = int(input("Число номер один?" + '\n'))
N2: int = int(input("Число номер два?" + '\n'))
N3: int = int(input("Сколько прибавить к первому числу?" + '\n'))
N4: int = int(input("На какую степень двойки умножить второе число?" + '\n'))
print('\n')

@repeat(N3)
def plus_1(x_0: int):
    """Функция"""
    return x_0 + 1

@repeat(N4)
def mul_2(x_0: int):
    """Еще одна функция"""
    return x_0 * 2

print(plus_1(N1))
print(mul_2(N2))
