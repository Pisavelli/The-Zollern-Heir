import time
from colorama import init, Fore, Style
from intro import show_intro, clear_screen

# Inicializa o colorama
init(autoreset=True)

# Mostra a introdução com arte
show_intro()

# Começa a narrativa
player = input("Digite seu nickname: ").upper()
clear_screen()

time.sleep(3)
print(f"{Fore.BLUE}No castelo de Zollern, o guerreiro {Fore.YELLOW}{player} {Fore.BLUE}representa o Conde que controla as redondezas, até que um dia...")
time.sleep(3)
print(f"{Fore.CYAN}SENTINELA: {Fore.WHITE}Vamos, {player}! Temos que sair daqui!")
time.sleep(3)
print(f"{Fore.YELLOW}{player}: {Fore.WHITE}Calma Guidowin, temos que defender o castelo.")
time.sleep(3)
print(f"{Fore.RED}GUIDOWIN: {Fore.WHITE}Desculpa, mas você não quis me escutar.")
time.sleep(3)
print(f"{Fore.RED}{Style.BRIGHT}GUIDOWIN empurra {player}, que acaba caindo da muralha e perde a consciência no rio...")
time.sleep(5)
clear_screen()
time.sleep(2)

print(f"{Style.DIM}DESCONHECIDO: Você está bem? Como veio parar aqui?")
time.sleep(5)
print(f"{Style.DIM}DESCONHECIDO: Vamos, você precisa repousar.")
time.sleep(3)
print(f"{Fore.YELLOW}{Style.DIM}{player}: U-ugh.")
time.sleep(2)
print(f"{Style.DIM}{player} é carregado para algum lugar...")
time.sleep(5)
print(f"{Fore.YELLOW}{Style.DIM}{player}: {Fore.WHITE}Onde... onde eu estou?")
print(f"{Style.DIM}DESCONHECIDO: Você está a salvo meu amigo, mas me deve explicações.")
