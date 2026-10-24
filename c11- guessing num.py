import random
secret=42
attempts=0
while attempts < 7:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print(f"Bravo! Found in {attempts} attempts")
        break
if guess!= secret:
    print("Lost! The secret was",secret)