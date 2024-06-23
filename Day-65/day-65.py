from typing import Any
import time

print("Generic RPG")
time.sleep(2)
print()

class Character:
    def __init__(self, name, health, magicPoints):
        self.name = name
        self.health = health
        self.magicPoints = magicPoints

    def talk(self):
        output = f"Name: {self.name} | Health: {self.health} | Magic Points: {self.magicPoints}"
        return output

class Player(Character):
    def __init__(self, nickname, lives, isAlive):
        super().__init__("Thomas", "110", "66")
        self.nickname = nickname
        self.lives = lives
        self.isAlive = isAlive

    def talk(self):
        base_output = super().talk()
        output = f"{base_output} | Nickname: {self.nickname} | Lives: {self.lives} | Alive: {self.isAlive}"
        print(output)

class Enemy(Character):
    def __init__(self, name, type, strength, health, magicPoints):
        super().__init__(name, health, magicPoints)
        self.type = type
        self.strength = strength
 
    def talk(self):
        base_output = super().talk()
        output = f"{base_output} | Type: {self.type} | Strength: {self.strength}"
        return output

class Orc(Enemy):
    def __init__(self, name, strength, health, magicPoints, speed):
        super().__init__(name, "Orc", strength, health, magicPoints)
        self.speed = speed

    def talk(self):
        base_output = super().talk()
        output = f"{base_output} | Speed: {self.speed}"
        print(output)

class Vampire(Enemy):
    def __init__(self, name, strength, health, magicPoints, day):
        super().__init__(name, "Vampire", strength, health, magicPoints)
        self.day = day

    def talk(self):
        base_output = super().talk()
        output = f"{base_output} | Day: {self.day}"
        print(output)

player = Player("tommy", "5", True)
orc = Orc("Gary", "20", "80", "30", "20%")
vampire = Vampire("Louis", "30", "60", "50", True)


player.talk()
orc.talk()
vampire.talk()

