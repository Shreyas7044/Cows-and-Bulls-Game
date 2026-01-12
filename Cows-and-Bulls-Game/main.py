# Cows and Bulls Game in Python

import random 

def getDigits(num):
    return [int(i) for i in str(num)]

def noDuplicates(num):
    return len(getDigits(num)) == len(set(getDigits(num)))

def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num

def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i, j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

# Game Start
secret_number = generateNum()
tries = int(input("Enter number of tries: "))

while tries > 0:
    guess = int(input("Enter your guess: "))

    if guess < 1000 or guess > 9999:
        print("Enter a 4-digit number only.")
        continue

    if not noDuplicates(guess):
        print("Digits must not repeat.")
        continue

    bulls, cows = numOfBullsCows(secret_number, guess)
    print(f"{bulls} bulls, {cows} cows")

    if bulls == 4:
        print("🎉 You guessed right!")
        break

    tries -= 1
else:
    print(f"❌ You ran out of tries. The number was {secret_number}")