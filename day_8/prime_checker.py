# check whether given number is prime

def prime_checker(number):
    for i in range (2,number):
        if number%i == 0:
            return "isn't"
    return "is"

n = int(input("Check this number: "))
print(f"{n} {prime_checker(number=n)} a prime number.")