import random
guess=str(random.randint(100,1001))
while True:
    inp = input('Enter any three digits: ')
    if len(inp) != 3:
        print('Number entered is not three digits, Please try again!')
        continue
    if guess[0] == inp[0] or guess[1] == inp[1] or guess[2] == inp[2]:
        print('Match')
    else:
        print('No Match')
    if guess == inp:
        print('Right Guess')
        break
