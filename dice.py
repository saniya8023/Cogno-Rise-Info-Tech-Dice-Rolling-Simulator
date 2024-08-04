import random

def roll_dice(sides, rolls):
    result = [random.randint(1, sides) for _ in range (rolls)]
    return result

def main():

    print('Welcome to Dice Rolling Simulator')

    sides = int(input('Enter your desired sides: '))

    rolls = int(input('Enter your desired rolls: '))

    result = roll_dice(sides, rolls)

    print('result of the simulation is:')
    for i, result in enumerate(result, start = 1):
        print(f'Roll {i} is {result}')

main()
