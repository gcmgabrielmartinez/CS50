import random

while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        pass
    else:
        target = random.randrange(1,n+1)
        break

#print(target)
guess = -1

while guess != target:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            raise ValueError
    except ValueError:
        pass
    else:
        if guess > target:
            print("Too large!")
            pass
        elif guess< target:
            print("Too small!")
            pass

print("Just right!")
exit()
