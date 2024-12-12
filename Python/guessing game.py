import random
secret_number = random.randint(1,10)
print("Please enter any number between One and Ten")
number_guess = input()
if secret_number == number_guess:
    print("You guessed correctly!!! Great job!")
else:
    print(secret_number)


