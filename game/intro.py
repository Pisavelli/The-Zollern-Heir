import shutil
import os
import sys
import time
import msvcrt

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.02):
    terminal = shutil.get_terminal_size()  # Tamanho do terminal
    width = terminal.columns  # Largura do terminal

    lines = text.split("\n")  # Divide o texto em várias linhas
    centered_text = [line.center(width) for line in lines]  # Centraliza cada linha

    # Para garantir que o texto centralize corretamente sem adicionar espaços em excesso
    for line in centered_text:
        for char in line:  # Imprime cada caractere com a pausa para o efeito de digitação lenta
            print(char, end="", flush=True)  # O 'end=""' evita que quebras de linha indesejadas ocorram
            time.sleep(delay)
    
    print()  # Adiciona uma nova linha ao final para separar o texto que vem depois

def wait_for_keypress():
    slow_print("\nPressione ENTER para jogar", delay=0.001)
    slow_print("Pressione ESC para sair", delay=0.001)

    while True:
        key = msvcrt.getch()
        if key == b'\r':  # ENTER
            return True
        elif key == b'\x1b':  # ESC
            clear_screen()
            print("Saindo do jogo...")
            time.sleep(2)
            sys.exit()

def show_intro():
    clear_screen()
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    banner_path = os.path.join(base_path, "assets", "banner.txt")

    try: # Ver se a pasta existe
        with open(banner_path, "r", encoding="utf-8") as f:
            title_art = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{banner_path}' não encontrado!")
        sys.exit()

    slow_print(title_art, delay=0.0015)

    if wait_for_keypress():
        clear_screen()
    else:
        clear_screen()
        print("Saindo do jogo...")
        time.sleep(2)
        sys.exit()

if __name__ == "__main__":
    show_intro()
