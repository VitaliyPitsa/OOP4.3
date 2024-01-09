#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, first, second):
        # Проверка корректности значений аргументов
        if first in [1, 2, 5, 10, 50, 100, 500, 1000, 5000] and second > 0:
            self.first = first
            self.second = second
        else:
            raise ValueError("Некорректные значения аргументов")

    def read(self):
        self.first = int(input("Введите номинал купюры: "))
        self.second = int(input("Введите количество купюр: "))

    def display(self):
        print(f"Номинал купюры: {self.first}")
        print(f"Количество купюр: {self.second}")

    def summa(self):
        return self.first * self.second

    def __add__(self, other):
        # Перегрузка оператора сложения
        if isinstance(other, Pair):
            if self.first == other.first:
                return Pair(self.first, self.second + other.second)
            else:
                raise ValueError("Номиналы купюр должны быть одинаковыми")
        else:
            raise TypeError("Неверный тип аргумента")

def make_Pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as e:
        print(str(e))
        exit()

if __name__ == '__main__':
    p1 = make_Pair(100, 5)
    p1.display()
    print(f"Сумма: {p1.summa()}")

    p2 = make_Pair(100, 3)
    p2.display()
    print(f"Сумма: {p2.summa()}")

    p3 = p1 + p2  # Использование перегруженного оператора сложения
    p3.display()
    print(f"Сумма: {p3.summa()}")