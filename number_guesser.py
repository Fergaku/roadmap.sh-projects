import random
# Number guesser game
print('Welcome to the number guesser game!')
print('I am thinking of a number between 1 and 100.')
print('Please select the difficulty.')
print('1. Easy: 10 attempts\n2. Medium: 5 attempts\n3. Hard: 3 attempts')

secret_num = random.randint(1, 100)
secret_num= int(secret_num)

attempts = 0
choice= int(input('Enter your choice: '))
while choice not in {1, 2, 3}:
    print('Invalid choice.')
    choice= int(input('Please select a valid difficulty: '))

match choice:
    case 1:
        attempts = 10
    case 2:
        attempts = 5
    case 3:
        attempts = 3
        
while attempts > 0:
    print('You have', attempts, 'attempts left.')
    try:
        guess =  int(input('Guess the number.'))
    except TypeError:
        print('Please enter a valid number.')
        continue
    if guess == secret_num:
        print('Congrats! You took,', attempts,'attempts, but you guessed the number!')
        break
    elif guess < secret_num:
        print('Your number is too low!')
        attempts -= 1
    elif guess > secret_num:
        print('Your number is too high!')
        attempts -= 1
if attempts == 0:
    print('You have run out of attempts. The number was:', secret_num)