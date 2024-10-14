def main():
    x = get_int("What is x?")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError: # except Exception as e                call e for error infos.         except alone will tank all Errors. but you can Search for more error type in the internet.
            pass
            print("x is no integer")

main()



