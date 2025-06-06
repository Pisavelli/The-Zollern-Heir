import ctypes
import os
import time
from intro import show_intro, clear_screen, slow_print
from character_creation import get_player_name, Character

def maximize_cmd(): # CMD
    os.system('mode con: cols=120 lines=40')
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, 3)

maximize_cmd()
show_intro()

# Usa a função para obter nome e confirmação
player_name = get_player_name()

# Cria o personagem
character = Character(player_name)

clear_screen()

time.sleep(3)
slow_print("No castelo de Zollern, vivia o Conde Bauyreth. Ele era um velho homem justo, que tratava seu povo com dignidade.")
time.sleep(5)
slow_print("O Conde Bauyreth era um homem humilde, que não se importava com casamentos arranjados.")
time.sleep(3)
slow_print("Uma vez, durante um baile da realeza aberto para os camponeses do condado, ele avistou uma jovem garota, Genevieve.")
time.sleep(2)
slow_print("Ele se apaixonou naquele instante. No entanto, ela era filha de um ferreiro.")
      
slow_print(f"SENTINELA: Vamos, {player_name}! Temos que sair daqui!")
time.sleep(5)
slow_print(f"{player_name}: Calma Guijnowin, temos que defender o castelo.")
time.sleep(5)
slow_print(f"GUIJNOWIN: Desculpa, mas você não quis me escutar.")
time.sleep(5)
slow_print(f"GUIJNOWIN empurra {player_name}, que acaba caindo da muralha e perde a consciência no rio...")
time.sleep(10)
clear_screen()
time.sleep(2)

slow_print(f"DESCONHECIDO: Você está bem? Como veio parar aqui?")
time.sleep(5)
slow_print(f"DESCONHECIDO: Vamos, você precisa repousar.")
time.sleep(3)
slow_print(f"{player_name}: U-ugh.")
time.sleep(2)
slow_print(f"{player_name} é carregado para algum lugar...")
time.sleep(5)
slow_print(f"{player_name}: Onde... onde eu estou?")
slow_print(f"DESCONHECIDO: Você está a salvo meu amigo, mas me deve explicações.")
