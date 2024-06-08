import sys


# noinspection PyUnreachableCode
def main():

    valid_commands = ["echo","exit 0"]

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        if user_command := input().strip():
            if user_command == "exit 0":
                break
                sys.exit(0)
            elif user_command.startswith("echo "):
                sys.stdout.write(user_command[5:] + "\n")
                sys.stdout.flush()
                continue
            if user_command not in valid_commands:
                sys.stdout.write(f"{user_command}: command not found\n")
                sys.stdout.flush()


if __name__ == "__main__":
    main()
