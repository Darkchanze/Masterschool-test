# Ask user for number input and return it.
def user_enter_number():
    number = input('Enter your number:')
    return number

# Loop as long as sum_of_numbers is not bigger 1000.
def count_number_until_1000():
    sum_of_numbers = 0
    while True:
        if sum_of_numbers > 1000:
            print(f'Final sum: {sum_of_numbers}')
            break
        sum_of_numbers = sum_of_numbers + int(user_enter_number()) # Add numbers from user input to the sum.

# Main: Program sequence.
def main():
    count_number_until_1000()

if __name__ == "__main__":
    main()