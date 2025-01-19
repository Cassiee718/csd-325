#Cassainy Noel 1/19/2025 3.2
import random, sys

# Dictionary for displaying dice numbers in Japanese
JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

# Introduction message
print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number. If you roll a 2 or a 7, then you
will receive a 10 mon bonus!
''')

# Starting amount for the player
purse = 5000

while True:  # Main game loop.
    # Ask the player how much they want to bet
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    
    while True:
        pot = input('CN: ')  # Input prompt changed to "CN:"
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)  # Convert pot to an integer.
            break  # Exit the loop once a valid bet is placed.

    # Roll the dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')

    # Let the player bet on cho or han
    while True:
        bet = input('CN: ').upper()  # Input prompt changed to "CN:"
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break

    # Reveal the dice results
    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    # Determine if the roll was even or odd
    rollIsEven = (dice1 + dice2) % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet

    # If the player won
    if playerWon:
        print('You won! You take', pot, 'mon.')
        
        # Check if the roll is a 2 or 7 and give the bonus
        if dice1 + dice2 == 2 or dice1 + dice2 == 7:
            print(f"Congrats! You rolled a {dice1 + dice2} and get a 10 mon bonus!")
            purse += 10  # Add bonus to the purse
        
        purse += pot  # Add the pot to the player's purse.
        
        # House fee changed to 12%
        house_fee = pot * 0.12
        print(f"The house collects a {house_fee} mon fee (12%).")
        purse -= house_fee  # Subtract the house fee (12%).
    else:
        purse -= pot  # Subtract the pot from player's purse.
        print('You lost!')

    # Check if the player has run out of money
    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()

