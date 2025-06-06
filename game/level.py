import random

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.next_level_up = 100  # XP necessário para subir do nível 1 → 2

    def acquire_xp(self, source):
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

        # Após ganhar XP:
        self.verify_level_up()
        self.display_status()

    def verify_level_up(self):
        while self.xp >= self.next_level_up:
            self.xp -= self.next_level_up
            self.level += 1
            self.next_level_up = int(self.next_level_up * 1.5)
            print(f"{self.name} subiu para o nível {self.level}!")

    def display_status(self):
        bar_length = 20
        progress = int((self.xp / self.next_level_up) * bar_length)
        barra = f"[{'#' * progress}{'-' * (bar_length - progress)}]"

        print(f"Nível: {self.level}")
        print(f"XP: {self.xp}/{self.next_level_up} {barra}")
        print("-" * 40)

# Teste com sequência de inimigos
player = Player()
inimigos = ["coelho", "lobo", "coelho", "coelho", "lobo", "coelho", "coelho", "lobo", "coelho", "coelho", "lobo", "coelho"]

for inimigo in inimigos:
    player.acquire_xp(inimigo)
