import os
import sys
import time
from colorama import init, Fore, Style

init(autoreset=True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def typewriter(text, delay):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def show_intro():
    clear_screen()

    # Lê o banner do arquivo externo
    with open("banner.txt", "r", encoding="utf-8") as f:
        title_art = f.read()

    print(Fore.YELLOW + Style.BRIGHT, end="")
    typewriter(title_art, delay=0.0015)
    print(Style.RESET_ALL)

    input("\nPressione ENTER para continuar...")
    clear_screen()

if __name__ == "__main__":
    show_intro()
