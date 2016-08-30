import random

#   initialise these at top for the whole program to use later
player1_hand = []
dealer_hand = []
player1_score = 0
dealer_score = 0


def get_deck():
    deck = [value + ' of ' + suit for value in '23456789TJQKA' for suit in 'SHDC']
    random.shuffle(deck)
    return iter(deck)

deck = get_deck()

values = {
        '2' : 2, '3': 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
        'T' : 10, 'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 11
        }

####    Score hands to an integer   ####
def score_hands(cards):
    sum = 0                     #Initialise integer sum
    for card in cards:          #For every card in all possible cards
        number = values[card[0]]    #Assign number with the value of each card string in values starting...
        sum += number              #at position zero. sum = sum + number to total every matching card up
    return sum


# def playagain():
#     print('Do you want to play again? (yes or no)')
#     return input().startswith('y')

##### START MAIN FUNCTION #####

print("Welcome to Blackjack, let's play! ")

#### Give out two cards to player1 and one to dealer ####

print("Your hand: ")
player1_hand.append(next(deck))
player1_hand.append(next(deck))
print(player1_hand)
player1_score = score_hands(player1_hand)
print(player1_score)

print("Dealer's hand: ")
dealer_hand.append(next(deck))
print(dealer_hand)
dealer_score = score_hands(dealer_hand)
print(dealer_score)
### askhit = hitNstick()

###    Hit and stick function    ####
#def hitNstick()    ### When I tried to implement this as a function, it wasn't happy with...
player_status = True    ### dealer_score for unknown reason.
while player_status:
    print("You have:\n")
    print(player1_score, player1_hand)

    if player1_score > 21:
        print("You're bust sir/madam!")

    if player_status:
        response = int(input("Do you want to Hit or Stick? (Hit = 1, Stay = 0)"))

        if response:
            player_status = True
            player1_hand.append(next(deck))
            print("You have drawn:\n")
            print(player1_hand)
            player1_score = score_hands(player1_hand)
            print(player1_score)
        else:
            player_status = False

    if player1_score <= 21:
        dealer_hand = '''\nDealer is at:\n'''
        print(dealer_hand, dealer_score)
    else:
        print("Dealer wins.")
        #playagain()

while dealer_score < 17:
        dealer_hand.append(next(deck))      #Throws up error "str object has no attribute 'append'
        print("Dealer has drawn:\n")
        print(dealer_hand)
        dealer_score = score_hands(dealer_hand)
        print(dealer_score)

        if dealer_score >= 17 and dealer_score < 22:
            break


####    Determine winner and loser  ####

if player1_score < 22 and dealer_score > 21:
    print ("You win!")
elif player1_score == dealer_score:
    print("Push - dealer wins.")
elif player1_score < dealer_score and dealer_score < 22:
    print("Dealer wins.")


