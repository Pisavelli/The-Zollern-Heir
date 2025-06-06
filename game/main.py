import ctypes
import os
import time
from intro import show_intro, clear_screen, typewriter

# Jogo executado no CMD
def maximize_cmd():
    os.system('mode con: cols=120 lines=40')  # Aumenta o tamanho do buffer
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, 3)  # 3 = SW_MAXIMIZE

# Mostra a introdução com arte
maximize_cmd()
show_intro()

# Começa a narrativa
player = input("Digite seu nickname: ").upper()
clear_screen()

time.sleep(3)
text = f"No castelo de Zollern, vivia o Conde Bauyreth. Ele era um velho homem justo, que tratava seu povo com dignidade."
typewriter(text, 0.075)
time.sleep(6)
print(f"O Conde Bauyreth era um homem humilde, que não se importava com casamentos arranjados.")
time.sleep(8)
print(f"Uma vez, durante um baile da realeza aberto para os camponeses do condado, ele avistou uma jovem garota, Genevieve.")
print(f"Uma vez, durante um baile da realeza aberto para os camponeses do condado, ele avistou uma jovem garota.")
      
print(f"SENTINELA: Vamos, {player}! Temos que sair daqui!")
time.sleep(5)
print(f"{player}: Calma Guijnowin, temos que defender o castelo.")
time.sleep(5)
print(f"GUIJNOWIN: Desculpa, mas você não quis me escutar.")
time.sleep(5)
print(f"GUIJNOWIN empurra {player}, que acaba caindo da muralha e perde a consciência no rio...")
time.sleep(10)
clear_screen()
time.sleep(2)

print(f"DESCONHECIDO: Você está bem? Como veio parar aqui?")
time.sleep(5)
print(f"DESCONHECIDO: Vamos, você precisa repousar.")
time.sleep(3)
print(f"{player}: U-ugh.")
time.sleep(2)
print(f"{player} é carregado para algum lugar...")
time.sleep(5)
print(f"{player}: Onde... onde eu estou?")
print(f"DESCONHECIDO: Você está a salvo meu amigo, mas me deve explicações.")
