import sys
import os
import subprocess

from typing import Optional

def locate_executable(command) -> Optional[str]:
    path = os.environ.get("PATH", "")
    for directory in path.split(":"):
        file_path = os.path.join(directory, command)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            return file_path
    return None

def action_echo(user_command):
    sys.stdout.write(user_command[5:] + "\n")
    sys.stdout.flush()

def action_exit(user_command):
    sys.exit(0)

def action_type(user_command):
    command = user_command[5:]
    command_path = locate_executable(command)
    if command in valids_commands:
        sys.stdout.write(f"{command} is a shell builtin\n")
    elif command_path:
        sys.stdout.write(f"{command} is {command_path}\n")
    else:
        command = command.split(":")[0]
        sys.stdout.write(f"{command}: not found\n")
    sys.stdout.flush()

def action_help(user_command):
    sys.stdout.write(f"Valid commands: {', '.join(valids_commands)}\n")
    sys.stdout.flush()

valids_commands = {"echo": action_echo,
                   "exit": action_exit,
                   "type": action_type,
                   "help": action_help}

# noinspection PyUnreachableCode
def main():

    # Loop para simular o shell
    while True:
        # Imprime o prompt
        sys.stdout.write("$ ")
        # Força a escrita do buffer
        sys.stdout.flush()

        PATH = os.getenv("PATH")

        # Lê a entrada do usuário
        if user_command := input().strip():
            # Separa o comando e os argumentos
            command, *args = user_command.split()
            # Verifica se o comando é válido
            if command in valids_commands:
                # Executa o comando
                valids_commands[command](user_command)
            else:
                # Executa o comando
                subprocess.run(user_command, shell=True)


if __name__ == "__main__":
    main()
