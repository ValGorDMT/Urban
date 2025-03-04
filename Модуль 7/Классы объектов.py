import random

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        print(f'{self.name} атакует {other.name}')
        other.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        print(f'{self.name} получает {damage} урона, осталось {self.health} очков здороья')

    def is_alive(self):
        return self.health > 0
    
class Warrior(Character):
    def __init__(self, name,):
        super().__init__(name, health=100, attack_power=20)

    def special_attack(self, other):
        damage = random.randint(5, self.attack_power * 2)
        print(f'{self.name} крушит {other.name}')
        other.take_damage(damage)


class Mage(Character):
    def __init__(self, name,):
        super().__init__(name, health=75, attack_power=15)

    def cast_spell(self, other):
        damage = random.randint(10, self.attack_power +10)
        print(f'{self.name} кастует молнию на {other.name}')
        other.take_damage(damage)


def battle(character1, character2):
    while character1.is_alive() and character2.is_alive():
       
        action = random.choice(['attack', 'spec_attack'])
        if isinstance(character1, Warrior) and action == 'spec_attack':
            character1.special_attack(character2)
        else:
            character1.attack(character2)
        if not character2.is_alive():
            print(f'{character2.name} побежден!')
            break

        action = random.choice(['attack', 'spec_attack'])
        if isinstance(character2, Warrior) and action == 'spec_attack':
            character2.special_attack(character1)
        else:
            character2.attack(character1)
        if not character1.is_alive():
            print(f'{character1.name} побежден!')
            break


def main():
    print('Добро пожаловать в приключения!')
    player_name = input('Введите имя вашего героя: ')
    choice = input('Выбирите класс (воин/маг)').lower
    if choice == 'воин':
        player = Warrior(player_name)
    elif choice == 'маг':
        player = Mage(player_name)
    else: 
        player = Warrior(player_name)
        print('Неверный выбор, вы теперь воин!')
    
    enemy = Warrior('Скелет-мечник')

    print(f'\n{player_name} вступает в сражение {enemy.name}')
    battle(player, enemy)


if __name__ == '__main__':
    main()
