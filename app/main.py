import sys


def main():

    valid_commands = []

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        user_command = input()
        if user_command not in valid_commands:
            sys.stdout.write(f"{user_command}: command not found\n")
            sys.stdout.flush()
        else:
            if user_command == "exit 0":
                break
                sys.exit(0)

if __name__ == "__main__":
    main()
