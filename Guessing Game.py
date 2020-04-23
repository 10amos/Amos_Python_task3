import random
easy = random.randint (1,10)
medium = random.randint (1,20)
hard = random.randint (1,50)

guessesTaken = 0
my_name = input("Welcome to Our Guessing Game, What is your name?\n ")
difficulty = input("Well, "+ my_name + ". What dificulty would you like ? easy medium or hard? \n")
if difficulty == "easy":
    number = easy
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 10\n")
    while guessesTaken < 6:
        guess = int(input('Take a guess. \n'))
        guessesTaken = guessesTaken + 1
        if guess == number:
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + my_name + '! You got it')
    if guess != number:
        number = str(number)
if difficulty == "medium":
    number = medium
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 20 \n")
    while guessesTaken < 4:
        guess = int(input('Take a guess. \n'))
        guessesTaken = guessesTaken + 1
        if guess == number:
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + my_name + '! You got it')
    if guess != number:
        number = str(number)
if difficulty == "hard":
    number = hard
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 50\n")
while guessesTaken < 3:
    guess = int(input('Take a guess. \n'))
    guessesTaken = guessesTaken + 1
    if guess == number:
        break
if guess == number:
    guessesTaken = str (guessesTaken)
    print('Good job, ' + my_name + '! You got it' )
if guess != number:
    number = str (number)
    print('Nope. The number I was thinking of was ' + number)
