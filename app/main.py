import sys


def main():

    valid_commands = []

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        user_command = input()
        if user_command not in valid_commands:
            sys.stdout.write(f"{user_command}: command not found\n")


if __name__ == "__main__":
    main()
