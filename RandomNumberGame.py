import random
randomNum = random.randint(1, 100)
counter = 1
print("I'm thinking of a number between 1 and 100. Guess it!")
guess = int(input("Your Guess: "))

while guess != randomNum:
    if guess > randomNum:
        print("Try a lower number.")
        guess = int(input("Your Guess:"))
        counter += 1
        #guess(randomNum, counter)
    elif guess < randomNum:
        print("Try a higher number.")
        guess = int(input("Your Guess:"))
        counter += 1
        #guess(randomNum, counter)
    if guess == randomNum:
        print("You guessed the number in ", counter, "tries.")
        print("Game over.")