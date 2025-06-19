def loja_vila(player, Health, Attack, Ducats, inventario):
    itens_loja = [
        {"nome": "Potion", "preco": 30, "efeito": "cura"},
        {"nome": "Sword", "preco": 25, "efeito": "attack"},
    ]

    while True:
        clear_screen()
        draw()
        slow_print("Você chegou a uma pequena vila. Um mercador se aproxima.")
        slow_print('"Olá, viajante! Deseja comprar algo?"')
        draw()
        slow_print(f"Você tem {Ducats} Ducats.")
        draw()
        for i, item in enumerate(itens_loja, 1):
            slow_print(f"{i} - {item['nome']} ({item['preco']} Ducats)")
        draw()
        slow_print("0 - Sair da loja")
        draw()

        try:
            escolha = int(input("> Escolha um item: "))
            if escolha == 0:
                break
            elif 1 <= escolha <= len(itens_loja):
                item = itens_loja[escolha - 1]
                if Ducats >= item["preco"]:
                    Ducats -= item["preco"]
                    inventario.append(item["nome"])
                    slow_print(f"Você comprou {item['nome']}!")
                    time.sleep(2)
                else:
                    slow_print("Você não tem Ducats suficientes.")
                    time.sleep(2)
            else:
                slow_print("Escolha inválida.")
                time.sleep(1.5)
        except ValueError:
            slow_print("Digite um número válido.")
            time.sleep(1.5)

    return Health, Attack, Ducats, inventario