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

    # Status do jogador
    Health = 12
    Attack = 1

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

            if about:
                slow_print("Este jogo foi criado para um projeto final de Raciocínio Algorítmico.")
                about = False
                choice = ""
                draw()

            choice = input("> ")

            if choice == "1":
                clear_screen()
                player = input("Qual seu nome?\n> ")
                clear_screen()
                slow_print(f"Bem-vindo, {player}.")
                time.sleep(3)
                menu = False
                play = True
                clear_screen()
                narrativa(player, Health, Attack) # Começa a narrativa após o jogador iniciar o jogo

            elif choice == "2":
                clear_screen()
                player, Health, Attack = load()
                slow_print(f"Bem-vindo novamente, {player}.")
                slow_print(input("> Pressione ENTER para continuar... "))
                menu = False
                play = True
                show_intro() # Exibe a introdução após carregar o jogo
                narrativa(player, Health, Attack) # Começa a narrativa ao carregar o jogo

            elif choice == "3":
                clear_screen()
                slow_print("Game project.")
                menu = False
                about = True

                while about:
                    dest = msvcrt.getch()
                    if dest == b'\x1b':  # ESC
                        about = False
                        menu = True

            elif choice == "4":
                clear_screen()
                print("Saindo...")
                time.sleep(2)
                close_cmd_window()

        while play:
            save(player, Health, Attack)  # Autosave

            draw()
            slow_print("SALVAR E SAIR - ESC")
            draw()

            dest = msvcrt.getch()

            if dest == b'\x1b':  # ESC
                play = False
                menu = True
                save(player, Health, Attack)



# Narrativa principal do jogo após iniciar o jogo no play
clear_screen()
def narrativa(player, Health, Attack):
    time.sleep(3)
    introducao = [
        "No castelo de Zollern, vivia o Conde Bauyreth. Ele era um velho homem justo, que tratava seu povo com dignidade.",
        "O Conde Bauyreth era um homem humilde, que não se importava com casamentos arranjados.",
        "Uma vez, durante um baile da realeza aberto para os camponeses do condado, ele avistou uma jovem garota, Genevieve.",
        "Ele se apaixonou naquele instante. No entanto, ela era filha de um ferreiro.",
        "Conde Bauyreth logo buscou benção de seu pai, no qual aceitou na hora.",
        "Muitas pessoas tinham inveja de Genevieve, almejando seu lugar como Condessa, os nobres sentiam nojo.",
        "Com o tempo, o Conde foi perdendo seu apoio e seus nobres planejavam esquemas de usurpar suas terras e seu título.",
        "Genevieve ficou grávida de um filho de Conde Bauyreth e, no momento do parto, acabou falecendo.",
        "A criança desse casamento ficaria isolada até seus 18 anos. O povo e os nobres nunca viram a criança após o nascimento."
    ]

    # Imprime a introdução linha por linha com a função centered_line()
    for linha in introducao:
        slow_print(linha)
        time.sleep(3)

    # Após a introdução, limpa a tela
    clear_screen()

    slow_print(f"SENTINELA: Vamos, {player}! Temos que sair daqui!")
    time.sleep(5)
    slow_print(f"{player}: Calma Guijnowin, temos que defender o castelo.")
    time.sleep(5)
    slow_print(f"GUIJNOWIN: Desculpa, mas você não quis me escutar.")
    time.sleep(5)
    slow_print(f"GUIJNOWIN empurra {player}, que acaba caindo da muralha e perde a consciência no rio...")
    time.sleep(10)
    clear_screen()
    time.sleep(2)

    slow_print(f"DESCONHECIDO: Você está bem? Como veio parar aqui?")
    time.sleep(5)
    slow_print(f"DESCONHECIDO: Vamos, você precisa repousar.")
    time.sleep(3)
    slow_print(f"{player} é carregado para algum lugar...")
    time.sleep(2)
    slow_print(f"{player}: U-ugh.")
    time.sleep(5)
    slow_print(f"{player}: Onde... onde eu estou?")
    slow_print(f"DESCONHECIDO: Você está a salvo meu amigo, mas me deve explicações.")

main()