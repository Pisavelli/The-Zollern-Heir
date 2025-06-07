from intro import clear_screen, slow_print
import random

class PlayerCharacter:
    def __init__(self, name):
        # Dados básicos
        self.name = name
        self.level = 1
        self.xp = 0
        self.next_level_up = 100

        # Atributos iniciais
        self.attributes = {
            'STR': 1,
            'HEA': 1,
            'DEF': 1,
            'CHA': 1
        }

        self.available_points = 0  # Pontos para distribuir após level up

    def acquire_xp(self, source):
        # Ganha XP ao derrotar inimigos
        xp_ranges = {
            "coelho": (5, 10),
            "lobo": (15, 25),
            "bandido": (30, 45)
        }

        if source.lower() in xp_ranges:
            xp_min, xp_max = xp_ranges[source.lower()]
            xp_acquired = random.randint(xp_min, xp_max)
        else:
            xp_acquired = 5

        self.xp += xp_acquired
        print(f"{self.name} derrotou um {source} e ganhou {xp_acquired} XP.")

        # Verifica se subiu de nível
        self.verify_level_up()
        self.display_status()

    def verify_level_up(self):
        # Se o XP for suficiente, sobe de nível e ganha pontos de atributo
        while self.xp >= self.next_level_up:
            self.level += 1
            self.xp -= self.next_level_up
            self.next_level_up = int(self.next_level_up * 1.5)
            self.available_points += 3
            print(f"\n{self.name} subiu para o nível {self.level}!")
            self.distribute_points()

    def display_status(self):
        # Barra de progresso do XP
        bar_length = 20
        progress = int((self.xp / self.next_level_up) * bar_length)
        barra = f"[{'#' * progress}{'-' * (bar_length - progress)}]"

        print(f"Nível: {self.level}")
        print(f"XP: {self.xp}/{self.next_level_up} {barra}")
        print("-" * 40)

    def display_character(self):
        print(f"Personagem: {self.name}")
        print("Atributos:")
        for attr, val in self.attributes.items():
            print(f"  {attr}: {val}")
        print(f"Pontos disponíveis para distribuir: {self.available_points}")
        
        # Limpa a tela após exibir os atributos
        input("\nPressione ENTER para continuar...")
        clear_screen()

    def distribute_points(self):
        # Distribuição dos pontos após subir de nível
        while self.available_points > 0:
            self.display_character()
            escolha = input("Escolha um atributo para aumentar (STR, HEA, DEF, CHA): ").upper()

            if escolha not in self.attributes:
                print("Atributo inválido. Tente novamente.")
                continue

            try:
                pontos = int(input(f"Quantos pontos deseja adicionar em {escolha}? "))
            except ValueError:
                print("Digite um número válido.")
                continue

            if pontos <= 0:
                print("Você precisa adicionar pelo menos 1 ponto.")
                continue

            if pontos > self.available_points:
                print(f"Você só tem {self.available_points} ponto(s).")
                continue

            self.attributes[escolha] += pontos
            self.available_points -= pontos

        print("Distribuição de atributos concluída!\n")
        self.display_character()

def get_player_name():
    while True:
        name = input("Digite o nome do personagem: ").strip().upper()
        if not name:
            print("Nome inválido, tente novamente.")
            continue

        confirm = input(f"Você digitou '{name}'. Está correto? (y/n): ").strip().lower()
        if confirm == 'y':
            return name.upper()
        elif confirm == 'n':
            clear_screen()
        else:
            print("Por favor, responda com 'y' ou 'n'.")
