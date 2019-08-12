import random
numguess = 0
name = input("hello please enter your name:")
number = random.randint(1,20)

print("Can you guess the number that I am thinking of (1-20)?",name)

while numguess < 6:
    print("Take a guess!")
    guess = input()
    guess = int(guess)

    numguess = numguess +1
    if guess <number:
        print("Number is too Low")
    if guess > number:
        print("Number is too High")
    if guess == number:
        break
if guess == number:
    numguess = str(numguess)
    print("Well Done!",name," you have guessed the number in",numguess,"times")

if guess != number:
    number = str(number)
    print("That is incorrect, the number was:", number)