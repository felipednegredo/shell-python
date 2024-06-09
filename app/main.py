import sys
import os
import subprocess

from typing import Optional


# Função para localizar um executável
def locate_executable(command) -> Optional[str]:
    # Verifica se o comando é um executável válido
    path = os.environ.get("PATH", "")
    for directory in path.split(":"):
        # Verifica se o arquivo existe e é executável
        file_path = os.path.join(directory, command)
        if os.path.isfile(file_path) and os.access(file_path, os.X_OK):
            # Retorna o caminho do arquivo
            return file_path
    return None


# Função para imprimir o texto após o comando echo
def action_echo(args):
    # Imprime o texto após o comando echo
    sys.stdout.write(' '.join(args[1:]) + "\n")
    # Força a escrita do buffer
    sys.stdout.flush()


# Função para finalizar o programa
def action_exit(args):
    # Finaliza o programa
    sys.exit(0)


# Função para verificar o tipo de um comando
def action_type(args):
    command = args[1]
    command_path = locate_executable(command)
    if command in valids_commands:
        sys.stdout.write(f"{command} is a shell builtin\n")
    elif command_path:
        sys.stdout.write(f"{command} is {command_path}\n")
    else:
        command = command.split(":")[0]
        sys.stdout.write(f"{command}: not found\n")
    sys.stdout.flush()


# Função para imprimir a lista de comandos válidos
def action_help(args):
    sys.stdout.write(f"Valid commands: {', '.join(valids_commands)}\n")
    sys.stdout.flush()


# Função para imprimir o diretório atual
def action_pwd(args):
    sys.stdout.write(os.getcwd() + "\n")
    sys.stdout.flush()


# Função para mudar de diretório
def action_cd(args):
    # Pega o diretório após o comando cd
    directory = ' '.join(args[1:])
    # Substitui ~ pelo diretório home
    directory = os.path.expanduser(directory)
    try:
        # Muda de diretório
        os.chdir(directory)
    except FileNotFoundError:
        # Se o diretório não existir, imprime a mensagem de erro
        sys.stdout.write(f"cd: {directory}: No such file or directory\n")
        sys.stdout.flush()


# Função para listar os arquivos de um diretório
def action_ls(args):
    # Pega o diretório após o comando ls
    directory = ' '.join(args[1:])
    # Substitui ~ pelo diretório home
    directory = os.path.expanduser(directory)
    try:
        # Lista os arquivos do diretório
        files = os.listdir(directory)
        # Imprime os arquivos
        sys.stdout.write("\n".join(files) + "\n")
    except FileNotFoundError:
        # Se o diretório não existir, imprime a mensagem de erro
        sys.stdout.write(f"ls: {directory}: No such file or directory\n")
    sys.stdout.flush()


# Dicionário com os comandos válidos
valids_commands = {"echo": action_echo,
                   "exit": action_exit,
                   "type": action_type,
                   "help": action_help,
                   "pwd": action_pwd,
                   "cd": action_cd,
                   "ls": action_ls}


# Função principal
def main():
    # Loop para simular o shell
    while True:
        # Imprime o prompt
        sys.stdout.write("$ ")
        # Força a escrita do buffer
        sys.stdout.flush()

        # Lê a entrada do usuário
        if user_command := input().strip():
            # Separa o comando e os argumentos
            args = user_command.split()
            # Verifica se o comando é válido
            if args[0] in valids_commands:
                # Executa o comando
                valids_commands[args[0]](args)
            else:
                # Executa o comando
                process = subprocess.run(user_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                if process.stderr:
                    error_message = process.stderr.decode('utf-8')
                    # Remove o /bin/sh: do início da mensagem de erro
                    error_message = error_message.replace('/bin/sh: ', '')

                    sys.stdout.write(error_message)
                    sys.stdout.flush()
                else:
                    sys.stdout.write(process.stdout.decode('utf-8'))
                    sys.stdout.flush()


if __name__ == "__main__":
    main()
