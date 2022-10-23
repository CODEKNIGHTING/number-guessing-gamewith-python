import random
start = input("type a number\n")
turns = 0
if start.isdigit():
    start = int(start)

if start <= 0:
    print("please type a bigger number than 0")
    quit()

number = random.randint(0, start)
while True:
    turns += 1
    guess = input("make a guess\n")
    if guess.isdigit:
        guess = int(guess)
    else:
        print("type a number")
        continue
    if guess == number:
        print('you got it')
        print("you got the number is " + str(turns) + " turns")
        break
    elif guess > number:
        print("you are above the number")
    else:
        print("your are below the number")