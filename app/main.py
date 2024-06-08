import sys


def main():

    sys.stdout.write("$ ")
    sys.stdout.flush()

    command = input()
    sys.stdout.write(f"{command} not found\r\n")


if __name__ == "__main__":
    main()
