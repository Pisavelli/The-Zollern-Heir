import time
from intro import slow_print
import random

# Representa um inimigo com nome, vida e XP
class Enemy:
    def __init__(self, name, health, xp_reward):
        self.name = name
        self.health = health
        self.xp_reward = xp_reward
    
    def battle(character, enemy):
        slow_print(f"\nUm {enemy.name} apareceu.")
        time.sleep(1)

        while enemy.health > 0:
            slow_print("\n{character.name} ataca você.")

            # Cálculo de dano com base na força (STR)
            dano = character.attributes["STR"] + random.randint(0, 2)
            enemy.health -= dano

            slow_print(f"{character.name} causo {dano} de dano.")
            if enemy.health <= 0:
                slow_print(f"\nO {enemy.name} foi derrotado.")
                character.acquire_xp(enemy.name)
                break
            else:
                slow_print(f"O {enemy.name} ainda tem {enemy.health} de vida.")
                time.sleep(1)