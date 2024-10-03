# Checking if one number is divisible through another number without reminder.
def is_divisible_by(number, by):
    if number % by == 0:
        return True
    else:
        return False

# Checking if a number is Prime.
def is_prime(number):
    count = 0
    for i in range(2, number):
        if is_divisible_by(number, i):
            count += 1  # If number is divisible by another number but itself and 1 this counter goes 1 up.
    if count > 0: # If this counter got bigger than 0 the number is no prime
        return False
    else:
        return True #Number is Prime

#Checking if a given range of numbers is Prime.
def primes_in_range(start, end):
    for i in range(start, end):
        if is_prime(i): #Checking if each number is Prime with the function 'is_prime'.
            print(f'The number {i} is prime')




# Main: Program sequence
def main():
    # Ask user to give start and end number to print out the print numbers in the given range.
    start = int(input('Enter start range: '))
    end = int(input('Enter end range: '))
    primes_in_range(start, end)


if __name__ == "__main__":
    main()