import random
guessesTaken=0
print('Hello! What is your name?')
myName = input()
hidden = random.randrange(1, 201)
print('Well, ' + myName + ', I am thinking of a number between 1 and 200.')
print(hidden)
while guessesTaken < 3:
    guess = int(input("Please enter your guess: "))
    guessesTaken = guessesTaken + 1
    if guess < hidden:
        print("your guess id too low!")
    elif guess> hidden:
        print("Your guess is too high")
    elif guess == hidden:
        print("COngratulations you guess Hidden number")
        break

