import sys
import os
import subprocess

# noinspection PyUnreachableCode
def main():

    # Lista de comandos válidos
    valid_commands = ["echo","exit","type","help"]

    # Loop para simular o shell
    while True:
        # Imprime o prompt
        sys.stdout.write("$ ")
        # Força a escrita do buffer
        sys.stdout.flush()

        PATH = os.getenv("PATH")

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
                command_path = None
                paths = PATH.split(":")
                for path in paths:
                    if os.path.exists(f"{path}/{command}"):
                        command_path = f"{path}/{command}"
                        break
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
                    # Imprime que o comando está no path
                    sys.stdout.write(f"{command} is {command_path}\n")
                continue
                # Se não for nenhum dos comandos acima, imprime que o comando não existe
            elif user_command == "help":
                sys.stdout.write(f"Valid commands: {', '.join(valid_commands)}\n")
            else:
                for path in PATH.split(":"):
                    if os.path.exists(f"{path}/{user_command}"):
                        subprocess.run(f"{path}/{user_command}")
                        break

            if user_command not in valid_commands:
                # Imprime que o comando não existe
                sys.stdout.write(f"{user_command}: command not found\n")
                # Força a escrita do buffer
                sys.stdout.flush()


if __name__ == "__main__":
    main()
