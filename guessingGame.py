print("WELCOME TO GUESS ME !")
print("I'm Thinking of a number between 1 and 100")
print("If your guess is less than 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll tell you you're COLD")
print("If your guess is closer than your most recent guess, I'll tell you you're WARM")
print("Let's play")

from random import randint

num = randint(0, 100)
# print("Gen num : ", num)
guesses = [0]

while True:
    guess = int(input("Guess any number between 1 to 100 : "))
    if guess < 1 or guess > 100:
        print("OUT OF BOUNDS")
        continue
    if guess == num:
        print("Congrats!! you have guessed the number correctly in just {} attempt.".format(len(guesses)))
        break
    guesses.append(guess)
    if guesses[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print("WARMER!!")
        else:
            print("COOLER!!")
    else:
        if abs(num - guess) <= 10:
            print("WARM!!!")
        else:
            print("COLD")
