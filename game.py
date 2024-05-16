# Игра "Бой"
#Создание абстрактного класса для оружия

from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

#  Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "удар мечом"

class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"

# Модификация класса Fighter

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon is not None:
            attack_message = self.weapon.attack()
            return f"{self.name} наносит {attack_message}."
        else:
            return f"{self.name} не вооружен."


class Monster:
    def __init__(self, name):
        self.name = name

    def defeat(self):
        return f"{self.name} побежден!"

# реализация  бооя

def battle(fighter, monster):
    print(fighter.attack())
    print(monster.defeat())


# Пример использования:
# Создаем бойца и монстра
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Создаем оружие
sword = Sword()
bow = Bow()

# Боец выбирает меч и атакует
fighter.change_weapon(sword)
print("Боец выбирает меч.")
battle(fighter, monster)

# Боец выбирает лук и атакует
fighter.change_weapon(bow)
print("Боец выбирает лук.")
battle(fighter, monster)
