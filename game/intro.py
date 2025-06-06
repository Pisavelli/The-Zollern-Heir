import os
import sys
import time
import msvcrt

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def typewriter(text, delay):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def wait_for_keypress():
    text = [f"\nPressione ENTER para jogar", "\nPressione ESC para sair"]
    typewriter(text, 0.075)

    while True:
        key = msvcrt.getch()
        if key == b'\r':   # ENTER
            return True
        elif key == b'\x1b':  # ESC
            clear_screen()
            # Show exit message, then close window
            print("Saindo do jogo...")
            time.sleep(2)
            # Close the window immediately
            import ctypes
            ctypes.windll.user32.PostQuitMessage(0)
            sys.exit()

def show_intro():
    clear_screen()
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    banner_path = os.path.join(base_path, "assets", "banner.txt")

    with open(banner_path, "r", encoding="utf-8") as f:
        title_art = f.read()

    typewriter(title_art, delay=0.0015)

    if wait_for_keypress():
        clear_screen()
    else:
        clear_screen()
        print("Saindo do jogo...")
        time.sleep(2)
        sys.exit()

if __name__ == "__main__":
    show_intro()
