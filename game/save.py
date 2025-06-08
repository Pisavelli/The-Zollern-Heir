import os

def save(player, health, attack):
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
        str(health),
        str(attack),
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
    health = int(load_list[1].strip())
    attack = int(load_list[2].strip())

    return player, health, attack
