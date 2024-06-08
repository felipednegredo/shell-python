import sys


# noinspection PyUnreachableCode
def main(user_commmand=None):

    valid_commands = []

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        user_command = input()
        if user_command == "exit 0":
            break
            sys.exit(0)
        elif user_commmand.startswith("echo"):
            sys.stdout.write(user_command[5:] + "\n")
            sys.stdout.flush()
        if user_command not in valid_commands:
            sys.stdout.write(f"{user_command}: command not found\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
