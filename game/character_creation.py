from intro import clear_screen, slow_print  # Importa suas funções já prontas

def get_player_name(): #Solicita o nome do personagem, com confirmação (y/n). Continua pedindo até receber um nome válido e confirmado.
    while True:
        name = input("Digite o nome do personagem: ").strip()
        if not name:
            print("Nome inválido, tente novamente.")
            continue

        confirm = input(f"Você digitou '{name}'. Está correto? (y/n): ").strip().lower()
        if confirm == 'y':
            return name.upper()  # Retorna o nome em maiúsculas
        elif confirm == 'n':
            clear_screen()  # Limpa a tela para o usuário digitar novamente
        else:
            print("Por favor, responda com 'y' ou 'n'.")

def show_attributes_description(): #Exibe uma explicação simples dos atributos para o jogador entender seu impacto.

    desc = """
Atributos do personagem:

STR (Força): Aumenta o dano causado.
AGI (Agilidade): Aumenta energia e velocidade de ataque.
INT (Inteligência): Permite aprender coisas novas.
CHA (Carisma): Facilita convencer pessoas.
"""
    slow_print(desc)

class Character:
    def __init__(self, name): # Inicializa o personagem com nome e atributos básicos no nível 1
        self.name = name
        self.attributes = {
            'STR': 1,
            'AGI': 1,
            'INT': 1,
            'CHA': 1
        }
        self.available_points = 0  # Pontos para distribuir ao subir de nível

    def display_character(self): # Mostra nome, atributos atuais e pontos disponíveis para distribuir
        print(f"\nPersonagem: {self.name}")
        print("Atributos:")
        for attr, val in self.attributes.items():
            print(f"  {attr}: {val}")
        print(f"Pontos disponíveis para distribuir: {self.available_points}")

    def level_up(self): # Quando sobe de nível, ganha 3 pontos para distribuir
        self.available_points += 3
        print(f"\n{self.name} subiu de nível! Você ganhou 3 pontos para distribuir.")

    def distribute_points(self): # Permite distribuir os pontos extras ganhos nos atributos
        while self.available_points > 0:
            print(f"\nPontos disponíveis: {self.available_points}")
            print("Atributos atuais:")
            for attr, val in self.attributes.items():
                print(f"  {attr}: {val}")

            escolha = input("Escolha o atributo para aumentar (STR, AGI, INT, CHA): ").upper()
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
                print(f"Você só tem {self.available_points} pontos disponíveis.")
                continue

            # Atualiza o atributo e diminui os pontos disponíveis
            self.attributes[escolha] += pontos
            self.available_points -= pontos

        print("\nDistribuição concluída!")
        self.display_character()

if __name__ == "__main__":
    clear_screen()
    slow_print("Bem-vindo a The Zollern Heir. Por favor crie seu personagem e divirta-se.\n")

    show_attributes_description()

    nome = get_player_name()
    character = Character(nome)
    clear_screen()
    character.display_character()
