#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Money:
    def __init__(self, size):
        self.size = size  # Максимальное количество элементов списка
        self.count = 0  # Текущее количество элементов списка
        self.amount = [0] * size  # Инициализация списка суммы денег

    def size(self):
        return self.size  # Возвращает максимальное количество элементов списка

    def add_digit(self, digit):
        if self.count < self.size:  # Если количество элементов списка не превышает максимальное
            self.amount[self.count] = digit  # Добавляем новую цифру к списку суммы
            self.count += 1  # Увеличиваем счетчик элементов списка
        else:
            print("Максимальная длина списка достигнута.")

    def add_penny(self, penny):
        if self.count + 2 <= self.size:  # Если количество элементов списка + 2 (копейки) не превышает максимальное
            self.amount[self.count] = penny // 10  # Добавляем цифру десятков к списку суммы
            self.amount[self.count + 1] = penny % 10  # Добавляем цифру единицы к списку суммы
            self.count += 2  # Увеличиваем счетчик элементов списка
        else:
            print("Максимальная длина списка достигнута.")

    def __str__(self):
        amount_str = ""
        for i in range(self.count):
            amount_str += str(self.amount[i])  # Преобразуем каждую цифру суммы в строку и добавляем к результату
        return amount_str  # Возвращает строковое представление суммы денег

    def __add__(self, other):
        if isinstance(other, Money):  # Проверяем, является ли other объектом класса Money
            max_size = max(self.size, other.size)  # Выбираем максимальное количество элементов списка из двух сумм
            result = Money(max_size)  # Создаем новый объект суммы денег с максимальным размером

            carry = 0  # Переменная для переноса разряда при сложении цифр
            for i in range(max_size):
                temp_sum = self.amount[i] + other.amount[i] + carry  # Суммируем цифры и перенос разряда
                result.amount[i] = temp_sum % 10  # Оставляем только единичный разряд и записываем в результат
                carry = temp_sum // 10  # Обновляем перенос разряда для следующей итерации

            if carry != 0:  # Если остался перенос разряда после сложения всех цифр
                result.add_digit(carry)  # Добавляем его к результату

            return result  # Возвращает новый объект суммы денег
        else:
            print("Операция '+' не поддерживается для данного типа.")


if __name__ == '__main__':

    #использованиe класса Money
    m1 = Money(100)
    m1.add_digit(5)
    m1.add_digit(7)
    m1.add_penny(99)
    print(m1)

