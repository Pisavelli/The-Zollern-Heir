def save_choices(choices):
    with open("choices.txt", "w", encoding="utf-8") as file:
        for choice in choices:
            file.write(choice + "\\n")
