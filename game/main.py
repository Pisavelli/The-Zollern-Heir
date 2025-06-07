import ctypes
import os
import time
from intro import show_intro, clear_screen, slow_print
from character_creation import get_player_name
from character_creation import PlayerCharacter

def maximize_cmd():  # Maximiza o terminal
    os.system('mode con: cols=100 lines=30') # largura x altura
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, 3)

maximize_cmd()
show_intro()

# Criação do personagem
player_name = get_player_name()
character = PlayerCharacter(player_name)

clear_screen()
character.display_character()

# Narrativa principal do jogo
time.sleep(3)
introducao = [
    "No castelo de Zollern, vivia o Conde Bauyreth. Ele era um velho homem justo, que tratava seu povo com dignidade.",
    "O Conde Bauyreth era um homem humilde, que não se importava com casamentos arranjados.",
    "Uma vez, durante um baile da realeza aberto para os camponeses do condado, ele avistou uma jovem garota, Genevieve.",
    "Ele se apaixonou naquele instante. No entanto, ela era filha de um ferreiro.",
    "Conde Bauyreth logo buscou benção de seu pai, no qual aceitou na hora.",
    "Muitas pessoas tinham inveja de Genevieve, almejando seu lugar como Condessa."
]

for linha in introducao:
    slow_print(linha)
    time.sleep(5)

slow_print(f"SENTINELA: Vamos, {character.name}! Temos que sair daqui!")
time.sleep(5)
slow_print(f"{character.name}: Calma Guijnowin, temos que defender o castelo.")
time.sleep(5)
slow_print(f"GUIJNOWIN: Desculpa, mas você não quis me escutar.")
time.sleep(5)
slow_print(f"GUIJNOWIN empurra {character.name}, que acaba caindo da muralha e perde a consciência no rio...")
time.sleep(10)
clear_screen()
time.sleep(2)

slow_print(f"DESCONHECIDO: Você está bem? Como veio parar aqui?")
time.sleep(5)
slow_print(f"DESCONHECIDO: Vamos, você precisa repousar.")
time.sleep(3)
slow_print(f"{character.name}: U-ugh.")
time.sleep(2)
slow_print(f"{character.name} é carregado para algum lugar...")
time.sleep(5)
slow_print(f"{character.name}: Onde... onde eu estou?")
slow_print(f"DESCONHECIDO: Você está a salvo meu amigo, mas me deve explicações.")


from battle import Enemy, battle  # ← adicione esse import

# ...continuação do main.py depois da história...
slow_print("\nUma sombra se move entre as árvores...")

# Criando um inimigo
coelho = Enemy("coelho", health=10, xp_reward=0)  # O XP real é tratado por nome dentro do acquire_xp

# Começa o combate
battle(character, coelho)
