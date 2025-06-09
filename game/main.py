import os, ctypes, time, msvcrt
from intro import slow_print, show_intro, clear_screen, close_cmd_window
from save import save, load

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
    char_width = 8   # Largura média de um caractere
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

def draw():
    print("────────────────────────")

# Função principal do jogo
def main():
    run = True
    menu = True
    play = False
    about = False
    key = False
    checkpoint = "prologo" # Checkpoint inicial

    # Status do jogador
    Health = 12
    Attack = 1
    Ducats = 0
    x = 0
    y = 0

    cmd_window() # Ajusta a janela do console
    show_intro()

    while run:
        while menu: # Exibe o menu
            clear_screen() # Limpa a tela antes de desenhar o menu
            draw()
            slow_print("1 - NOVO JOGO")
            slow_print("2 - CARREGAR JOGO")
            slow_print("3 - SOBRE")
            slow_print("4 - SAIR")
            draw()

            choice = input("> ")

            if choice == "1":
                clear_screen()

                while True:
                    player = input("Qual seu nome?\n> ").strip()
                    if player:
                        break
                    else:
                        slow_print("Por favor, insira um nome válido.")
                        time.sleep(1)
                        clear_screen()

                slow_print(player)
                clear_screen()
                slow_print(f"Bem-vindo, {player}.")
                time.sleep(3)

                menu = False
                play = True
                clear_screen()
                checkpoint, play, menu = narrativa(player, Health, Attack, Ducats, x, y, key, checkpoint) # Começa a narrativa após o jogador iniciar o jogo

            elif choice == "2":
                clear_screen()

                player, Health, Attack, Ducats, x, y, key, checkpoint = load()
                slow_print(f"Bem-vindo novamente, {player}.")
                slow_print(input("> Pressione ENTER para continuar... "))
                clear_screen()

                menu = False
                play = True
                checkpoint, play, menu = narrativa(player, Health, Attack, Ducats, x, y, key, checkpoint) # Começa a narrativa ao carregar o jogo

            elif choice == "3":
                clear_screen()
                menu = False
                about = True

                slow_print("Este jogo foi criado para um projeto final de Raciocínio Algorítmico.")
                slow_print("\n> Pressione ESC para voltar ao menu.")
                
                while about:
                    if msvcrt.kbhit():
                        key = msvcrt.getch()
                        if key == b'\x1b': # ESC
                            about = False
                            menu = True
                            
            elif choice == "4":
                clear_screen()

                print("Saindo...")
                time.sleep(2)
                close_cmd_window()

        while play:
            save(player, Health, Attack, Ducats, x, y, key, checkpoint)  # Autosave

            draw()
            slow_print("SALVAR E SAIR - ESC")
            draw()

            dest = msvcrt.getch()

            if dest == b'\x1b':  # ESC
                play = False
                menu = True
                save(player, Health, Attack, Ducats, x, y, key, checkpoint)



# Narrativa principal do jogo após iniciar o jogo no play
clear_screen()
def narrativa(player, Health, Attack, Ducats, x, y, key, checkpoint):
    if checkpoint == "prologo":
        time.sleep(3)

        # PRÓLOGO
        prologo = [
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
        for linha in prologo:
            slow_print(linha)
            time.sleep(3)

        # Após o prólogo, limpa a tela
        clear_screen()

        checkpoint = "introducao"
        save(player, Health, Attack, Ducats, x, y, key, checkpoint)

    if checkpoint == "introducao":
        time.sleep(3)

        # INTRODUÇÃO
        introducao = [
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
        clear_screen()
        introducao = [
            "Você ouve algo.",
            "DESCONHECIDO: Você está bem? Como veio parar aqui?",
            "DESCONHECIDO: Vamos, você precisa repousar.",
            f"Você é carregado para algum lugar...",
            f"{player}: U-ugh.",
            f"{player}: Onde... onde eu estou?",
            "DESCONHECIDO: Você está a salvo meu amigo, mas me deve explicações."
        ]
        
        # Imprime a introdução linha por linha
        for linha in introducao:
            slow_print(linha)
            time.sleep(3)
            
        # Após a introdução, limpa a tela
        clear_screen()

        checkpoint =  "inicio"
        save(player, Health, Attack, Ducats, x, y, key, checkpoint)

    if checkpoint == "inicio":
        time.sleep(3)

        # INÍCIO DO JOGO
        inicio = [
            "Você sente cheiro de comida.",
            "DESCONHECIDO: Bom dia, levante-se e venha comer.",
            "Você levanta da cama, vai em direção a mesa e senta na cadeira."
            ]
        
        # Imprime o início linha por linha
        for linha in inicio:
            slow_print(linha)
            time.sleep(3)
            
        draw()
        slow_print("1 - QUEM É VOCÊ?")
        slow_print("2 - ONDE EU ESTOU?")
        draw()
        slow_print("ESC - SALVAR E VOLTAR AO MENU")
        draw()
        
        while True:
            if msvcrt.kbhit():
                key = msvcrt.getch() # Get a tecla que é pressionada pelo usuário
                if key == b'\x1b': # ESC
                    clear_screen()
                    print("Salvando e voltando ao menu...")
                    time.sleep(2)
                    save(player, Health, Attack, Ducats, x, y, key, checkpoint)
                    return checkpoint, False, True # play=False, menu=True
            
            elif key == b'1':
                clear_screen()
                slow_print(f"{player}: Quem é você?")
                break
            
            elif key == b'2':
                clear_screen()
                slow_print(f"{player}: Onde estou?")
                break

    return checkpoint, True, False # Continua jogando
main()
