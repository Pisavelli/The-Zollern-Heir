import os, ctypes, time, msvcrt, sys

#  Função que ajusta o tamanho da janela do console no Windows
def cmd_window(cols=130, lines=50):
    # Define o tamanho da janela do console
    os.system(f"mode con: cols={cols} lines={lines}")

    # Acessa funções do Windows
    user32 = ctypes.windll.user32
    kernel32 = ctypes.windll.kernel32

    # Tamanho da tela (resolução do monitor)
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    # Tamanho da janela do console (aproximado)
    char_width = 8  # Largura média de um caractere
    char_height = 16  # Altura média de um caractere
    window_width = cols * char_width
    window_height = lines * char_height

    # Posição no centro
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)

    # Obtém handle da janela do console
    hWnd = kernel32.GetConsoleWindow()

    # Move a janela para o centro da tela
    ctypes.windll.user32.MoveWindow(hWnd, x, y, window_width, window_height, True)

#  Função que carrega a tela do jogo, limpa a tela e imprime o título do jogo
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

def draw():
    slow_print("────────────────────────")

def wait_for_keypress():
    draw()
    choice = ["> Press ENTER to continue", "> Press ESC to exit"]
    for line in choice:
        slow_print(line, delay=0.0015)
    draw()
    while not msvcrt.kbhit():
        time.sleep(10)

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

#  Funções que salvam e carregam o jogo
def save(player, Health, Attack, Ducats, x, y, checkpoint):
    # Obtém o diretório onde o script está sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Define o diretório de salvamento dentro da pasta 'save' do jogo
    save_dir = os.path.join(base_dir, "save")

    # Verifica se a pasta 'save' existe, se não, cria
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    # Define o caminho completo do arquivo de salvamento
    file_path = os.path.join(save_dir, "load.txt")

    # Lista com os dados a serem salvos
    list = [
        player,
        str(Health),
        str(Attack),
        str(Ducats),
        str(x),
        str(y),
        str(checkpoint)
    ]

    # Abre o arquivo e escreve os dados
    with open(file_path, "w") as f:
        for item in list:
            f.write(item + "\n")

def load():
    # Obtém o diretório onde o script está sendo executado
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Define o caminho para a pasta 'save' e o arquivo 'load.txt'
    save_dir = os.path.join(base_dir, "save")
    file_path = os.path.join(save_dir, "load.txt")

    # Verifica se o arquivo de salvamento existe
    if not os.path.exists(file_path):
        print("Arquivo de salvamento não encontrado!")
        return None, None, None  # Retorna valores padrões se o arquivo não existir

    # Abre o arquivo de salvamento e lê os dados
    with open(file_path, "r") as f:
        load_list = f.readlines()

    # Processa os dados lidos
    player = load_list[0].strip()
    Health = int(load_list[1].strip())
    Attack = int(load_list[2].strip())
    Ducats = int(load_list[3].strip())
    x = int(load_list[4].strip())
    y = int(load_list[5].strip())
    checkpoint = load_list[6].strip()

    return player, Health, Attack, Ducats, x, y, checkpoint

#  Função que desenha a borda dos menus
def draw():
    slow_print("────────────────────────")

#  Função que exibe o menu principal do jogo
def show_menu():
    clear_screen()  # Limpa a tela antes de desenhar o menu
    draw()
    slow_print("1 - NEW GAME")
    slow_print("2 - LOAD GAME")
    slow_print("3 - ABOUT GAME")
    draw()
    slow_print("4 - LEAVE GAME")
    draw()

#  Função que salva o jogo e retorna ao menu
def save_and_return_to_menu(player, Health, Attack, Ducats, x, y, checkpoint):
    save(player, Health, Attack, Ducats, x, y, checkpoint) # Save
    clear_screen()
    slow_print("SAVING AND RETURNING TO MENU...")
    time.sleep(2)
    return "menu", False, True  # play=False, menu=True

#  Função que exibe o menu de pausa do jogo
def pause_menu(player, Health, Attack, Ducats, x, y, checkpoint):
    while True:
        clear_screen()
        draw()
        slow_print("PAUSE MENU")
        draw()
        slow_print("1 - CONTINUE GAME")
        slow_print("2 - SAVE GAME")
        slow_print("3 - LOAD GAME")
        slow_print("4 - BACK TO MENU")
        draw()

        choice = input("> ").strip().upper()
        if choice == "1":  # CONTINUE GAME
            clear_screen()
            return True
        elif choice == "2":  # SAVE GAME
            clear_screen()
            save(player, Health, Attack, Ducats, x, y, checkpoint)
            slow_print("Game saved!")
            time.sleep(1)
        elif choice == "3":  # LOAD GAME
            if not os.path.exists("save.txt"):
                clear_screen()
                slow_print("No saved game found.")
                slow_print("> Press any key to continue...")
                input("> ")  # Espera o usuário pressionar qualquer tecla
                continue
            player, Health, Attack, Ducats, x, y, checkpoint = load()
            slow_print(f"Game loaded, {player}.")
            time.sleep(2)
        elif choice == "4":  # BACK TO MENU
            slow_print("Save game before returning to the menu? (Y/N)")
            while True:
                choice = input("> ").strip().upper()
                if choice == "Y":
                    save(player, Health, Attack, Ducats, x, y, checkpoint)
                    slow_print("Game saved!")
                    time.sleep(1)
                    return False
                elif choice == "N":
                    slow_print("Returning to menu without saving...")
                    time.sleep(1)
                    return False

# Função principal do jogo
def main():
    run = True
    menu = True
    submenu = False
    play = False
    checkpoint = "prologue"  # Checkpoint inicial

    # Status do jogador
    Health = 12
    Attack = 1
    Ducats = 0
    x = 0
    y = 0

    cmd_window()  # Ajusta a janela do console
    show_intro()

    while run:
        while menu:  # Exibe o menu
            show_menu()

            # Espera até alguma tecla ser pressionada
            while not msvcrt.kbhit():
                time.sleep(10)

            key = input("> ").strip().upper()  # Lê a tecla pressionada
            if key == "":  # Se nenhuma tecla foi pressionada
                continue

            if key == "1":  # Novo jogo
                clear_screen()
                while True:
                    draw()
                    slow_print("4 - BACK TO MENU")
                    draw()
                    slow_print("What is your name?")
                    draw()
                    player = input("> ").strip().upper()  # Lê o nome do jogador e converte para maiúsculas
                    if player and player.isalpha():  # Verifica se o nome é válido (não vazio e contém apenas letras)
                        break
                    else:
                        slow_print("Please enter a valid name.")
                        time.sleep(1)
                        clear_screen()

                slow_print(player)
                clear_screen()
                slow_print(f"Welcome, {player}.")
                time.sleep(3)
                clear_screen()

                menu = False
                play = True
                checkpoint, play, menu = narrativa(player, Health, Attack, Ducats, x, y, checkpoint)  # Começa a narrativa após o jogador iniciar o jogo
                break

            elif key == "2":  # Carregar jogo
                if not os.path.exists("save.txt"):
                    clear_screen()
                    slow_print("No saved game found.")
                    slow_print("> Press any key to continue...")
                    while not msvcrt.kbhit():
                        time.sleep(10)
                    msvcrt.getch()
                    continue
                clear_screen()
                player, Health, Attack, Ducats, x, y, checkpoint = load()
                slow_print(f"Welcome back, {player}.")
                slow_print("> Press any key to continue...")
                while not msvcrt.kbhit():
                    time.sleep(10)
                msvcrt.getch()
                clear_screen()

                menu = False
                play = True
                checkpoint, play, menu = narrativa(player, Health, Attack, Ducats, x, y, checkpoint)  # Começa a narrativa ao carregar o jogo
                break

            elif key == "3":  # ABOUT GAME
                clear_screen()
                submenu = True
                draw()
                slow_print("This game was created for the final project of Algorithmic Reasoning.")
                draw()
                slow_print("> Press any key to continue...")
                draw()

                while submenu:
                    while not msvcrt.kbhit():
                        time.sleep(1)
                    msvcrt.getch()
                    clear_screen()
                    break  # Força o loop while menu a reiniciar, redesenhando o menu

            elif key == "4":  # BACK TO MENU
                clear_screen()
                print("Exiting...")
                time.sleep(2)
                close_cmd_window()
                return  # Finaliza o jogo corretamente
            
            else:
                print("Invalid option. Please try again.")
                time.sleep(2)
                                                    
        while play:
            draw()
            slow_print("4 - SAVE AND EXIT")
            draw()

            key = input("> ").strip().upper()  # Lê a tecla pressionada
            if key == "":  # Se nenhuma tecla foi pressionada
                continue
            if key == "4":  # SAVE AND EXIT
                checkpoint, play, menu = save_and_return_to_menu(player, Health, Attack, Ducats, x, y, checkpoint)
            
# Narrativa principal do jogo após iniciar o jogo no play
def narrativa(player, Health, Attack, Ducats, x, y, checkpoint):
    if checkpoint == "prologue":
        time.sleep(3)

        # PRÓLOGO
        prologue = [
            "No castelo de Zollern, vivia o Conde Bauyreth. Ele era um homem justo, que tratava seu povo com dignidade.",
            "O Conde Bauyreth era um homem humilde, que não se importava com casamentos arranjados.",
            "Uma vez, durante um baile da realeza aberto para os camponeses do condado, ele avistou uma jovem garota, Genevieve.",
            "Ele se apaixonou naquele instante. No entanto, ela era filha de um ferreiro.",
            "Conde Bauyreth logo buscou benção de seu pai, o qual aceitou na hora.",
            "Muitas pessoas tinham inveja de Genevieve, almejando seu lugar como Condessa, os nobres sentiam nojo.",
            "Com o tempo, o Conde foi perdendo seu apoio e seus nobres planejavam esquemas de usurpar suas terras e seu título.",
            "Genevieve ficou grávida de um filho de Conde Bauyreth e, no momento do parto, acabou falecendo.",
            "A criança desse casamento ficaria isolada até seus 18 anos. O povo e os nobres nunca viram a criança após o nascimento."
            ]
        
        # Imprime o prólogo linha por linha
        for linha in prologue:
            slow_print(linha)
            time.sleep(3)

        # Após o prólogo, limpa a tela
        clear_screen()

        checkpoint = "intro1"
        save(player, Health, Attack, Ducats, x, y, checkpoint)

    if checkpoint == "intro1":
        time.sleep(3)

        # INTRODUÇÃO - PARTE 1
        intro1 = [
            f"DESCONHECIDO: Vamos, {player}! Temos que sair daqui!",
            f"{player}: Calma Guijnowin, ainda temos chance.",
            "GUIJNOWIN: Chance? Você deveria ir enquanto há tempo! Vai!",
            f"{player}: Temos vantagem defensiva, só precisamos esperar os reforços chegarem!",
            "GUIJNOWIN: Não acredito que os reforços cheguem. Além disso, nós dois não seguraremos o castelo sozinhos.",
            f"GUIJNOWIN: {player}, você me agradecerá depois.",
            f"{player}: O quê?",
            f"GUIJNOWIN dá um chute em seu tórax, que faz você cair da muralha em direção ao rio.",
            "Você perde consciência.",
            ]
        # Imprime a introdução parte 1 linha por linha
        for line in intro1:
            slow_print(line)
            time.sleep(3)

        # Após a introdução, limpa a tela
        clear_screen()

        checkpoint = "intro2"
        save(player, Health, Attack, Ducats, x, y, checkpoint)

    if checkpoint == "intro2":
        time.sleep(3)

        # INTRODUÇÃO - PARTE 2
        intro2 = [
            "Você ouve algo.",
            "DESCONHECIDO: Você está bem? Como veio parar aqui?",
            "DESCONHECIDO: Vamos, você precisa repousar.",
            f"Você é carregado para algum lugar...",
            f"{player}: U-ugh.",
            f"{player}: Onde... onde eu estou?",
            "DESCONHECIDO: Você está a salvo meu amigo, mas me deve explicações."
        ]
        
        # Imprime a introdução parte 2 linha por linha
        for line in intro2:
            slow_print(line)
            time.sleep(3)
            
        # Após a introdução, limpa a tela
        clear_screen()

        checkpoint =  "part1"
        save(player, Health, Attack, Ducats, x, y, checkpoint)

    if checkpoint == "part1":
        time.sleep(3)

        # INÍCIO DO JOGO
        part1 = [
            "Você sente cheiro de comida.",
            "DESCONHECIDO: Bom dia, levante-se e venha comer.",
            "Você levanta da cama, vai em direção a mesa e senta na cadeira."
            ]
        
        # Imprime o início linha por linha
        for line in part1:
            slow_print(line)
            time.sleep(3)
            
        draw()
        slow_print("1 - WHO ARE YOU?")
        slow_print("2 - WHERE AM I?")
        draw()
        slow_print("3 - SAVE AND RETURN TO MENU")
        draw()
        
        while True:
            pressed = None  # <- Garante que 'pressed' existe sempre
            if msvcrt.kbhit():
                pressed = msvcrt.getch()  # Get a tecla que é pressionada pelo usuário
                
                if pressed == b'\x1b':  # ESC
                    save(player, Health, Attack, Ducats, x, y, checkpoint)
                    clear_screen()
                    print("Salvando e voltando ao menu...")
                    time.sleep(2)
                    return checkpoint, False, True  # play=False, menu=True
            
                elif pressed == b'1':
                    clear_screen()
                    slow_print(f"{player}: Quem é você?")
                    break
            
                elif pressed == b'2':
                    clear_screen()
                    slow_print(f"{player}: Onde estou?")
                    break

    return checkpoint, True, False  # Continua jogando
main()


# CONTINUAR E FOCAR ENREDO;
# Fazer inventário;
# Fazer level up;
# Fazer lojas.