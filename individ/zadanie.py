#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random

class Soldier:
    def __init__(self, number, team):
        self.number = number
        self.team = team  # команда, к которой принадлежит солдат

    def follow_hero(self, hero):
        # Метод "иду за героем", принимает объект типа "герой"
        print(f"Солдат {self.number} идет за героем {hero.number}")

class Hero:
    def __init__(self, number, team):
        self.number = number
        self.team = team  # команда, к которой принадлежит герой
        self.level = 1  # уровень героя

    def increase_level(self):
        # Метод увеличивает уровень героя
        self.level += 1

if __name__ == '__main__':

    # Создание героев для каждой команды
    hero1 = Hero(1, "Команда 1")
    hero2 = Hero(2, "Команда 2")

    # Списки для солдат каждой команды
    soldiers_team1 = []
    soldiers_team2 = []

    # Генерация случайных солдат
    for i in range(10):
        soldier = Soldier(i, random.choice(["Команда 1", "Команда 2"]))
        if soldier.team == "Команда 1":
            soldiers_team1.append(soldier)
        else:
            soldiers_team2.append(soldier)

    # Вывод длины списков солдат противоборствующих команд
    print("Длина списка солдат Команды 1:", len(soldiers_team1))
    print("Длина списка солдат Команды 2:", len(soldiers_team2))

    # Увеличение уровня героя команды с более длинным списком солдат
    if len(soldiers_team1) > len(soldiers_team2):
        hero1.increase_level()
    else:
        hero2.increase_level()

    # Отправка одного из солдат первого героя следовать за ним
    soldier_to_follow = random.choice(soldiers_team1)
    hero1.follow_hero(soldier_to_follow)

    # Вывод идентификационных номеров этих двух юнитов
    print(f"Идентификационный номер солдата: {soldier_to_follow.number}")
    print(f"Идентификационный номер героя: {hero1.number}")
