import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return f'{self.name} получил {amount} урона. Текущее здоровье: {self.health}'
    
    def heal(self, amount):
        pass

class Room:
    def __init__(self, desc):
        self.desc = desc
        self.items = []
        self.enemy = None

    def add_item(self, item):
        self.items.append(item)
        return f'В комнату добавлен предмет: '
    
    def set_enemy(self, enemy):
        self.enemy = enemy

    def show_enemy(self):
        if self.enemy:
            return f'Вы встретили врага {self.enemy.name}, его здоровье: {self.enemy.health}'
        return 'Врагов нет'

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health =health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        return f'{self.name} получил {amount} урона. Текущее здоровье: {self.health}'
    

rooms = [
    Room('Болото'),
    Room('Озеро'),
    Room('Склад'),
    Room('Цитадель')
]


enemies = [
    Enemy('Змея'),
    Enemy('Единорог'),
    Enemy('Тролль'),
    Enemy('Гоблин'),
]


hero = Player('Slarck')