import os
import sys
import time
import msvcrt
import ctypes

def clear_screen(): # Limpa a tela
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.02): # Efeito de escrita
    lines = text.split("\n")
    for line in lines:
        for char in line:
            print(char, end="", flush=True)
            time.sleep(delay)
        print()

def close_cmd_window(): # Fecha completamente a janela do CMD (Windows)
    kernel32 = ctypes.windll.kernel32
    user32 = ctypes.windll.user32
    hWnd = kernel32.GetConsoleWindow()
    user32.PostMessageW(hWnd, 0x0010, 0, 0)  # Envia mensagem WM_CLOSE (fechar janela)

def wait_for_keypress():
    opcoes = ["\n> Pressione ENTER para continuar", "> Pressione ESC para sair"]
    for linha in opcoes:
        slow_print(linha)

    while True:
        key = msvcrt.getch() # Get a tecla que é pressionada pelo usuário
        if key == b'\r':  # ENTER
            return True
        elif key == b'\x1b':  # ESC
            clear_screen()
            print("Saindo...")
            time.sleep(2)
            close_cmd_window()

def show_intro(): # Intro com o nome do jogo The Zollern Heir
    clear_screen()
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    banner_path = os.path.join(base_path, "assets", "banner.txt")

    try:
        with open(banner_path, "r", encoding="utf-8") as f:
            title_art = f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{banner_path}' não encontrado!")
        time.sleep(2)
        sys.exit()

    slow_print(title_art, delay=0.0015)

    if wait_for_keypress():
        clear_screen()

if __name__ == "__main__":
    show_intro()
