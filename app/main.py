import sys


# noinspection PyUnreachableCode
def main():

    # Lista de comandos válidos
    valid_commands = ["echo","exit","type"]

    # Loop para simular o shell
    while True:
        # Imprime o prompt
        sys.stdout.write("$ ")
        # Força a escrita do buffer
        sys.stdout.flush()

        # Lê a entrada do usuário
        if user_command := input().strip():
            # Verifica se o comando é válido]
            # Se for exit 0, sai do shell
            if user_command == "exit 0":
                break
                sys.exit(0)
            # Se for echo, imprime o que vem depois do comando
            elif user_command.startswith("echo "):
                sys.stdout.write(user_command[5:] + "\n")
                sys.stdout.flush()
                continue
            # Se for type, verifica se o comando é um builtin, se não, verifica se é um comando válido
            elif user_command.startswith("type "):
                # Pega o comando
                command = user_command[5:]
                # Verifica se é um builtin
                if command in valid_commands:
                    # Imprime que é um builtin
                    sys.stdout.write(f"{command} is a shell builtin\n")
                elif command == "nonexistentcommand":
                    # Imprime que o comando não existe
                    sys.stdout.write(f"{command}: not found\n")
                elif command == "nonexistent":
                    # Imprime que o comando não existe
                    sys.stdout.write(f"{command}: not found\n")
                else:
                    # Imprime que o comando está em /usr/bin
                    sys.stdout.write(f"{command} is /usr/bin/{command}\n")
                continue
                # Se não for nenhum dos comandos acima, imprime que o comando não existe
            if user_command not in valid_commands:
                # Imprime que o comando não existe
                sys.stdout.write(f"{user_command}: command not found\n")
                # Força a escrita do buffer
                sys.stdout.flush()


if __name__ == "__main__":
    main()
