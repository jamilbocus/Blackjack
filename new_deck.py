import random

def get_deck():
    deck = [value + ' of ' + suit for value in '23456789TJQKA' for suit in 'SHDC']
    random.shuffle(deck)
    return iter(deck)

values = {
        '2' : 2, '3': 3, '4' : 4, '5' : 5, '6' : 6, '7' : 7, '8' : 8, '9' : 9,
        'T' : 10, 'J' : 10, 'Q' : 10, 'K' : 10, 'A' : 11
        }



def score(list):
    sum = 0
    for card in list:
        number = values[card[0]]
        sum += number
    return sum
#player
# while true
#     if hit

        #continue
#     if stick
#         break
#dealer
# while true
#     if less than 17
#         hit
#
#     elif more than 21
#         bust
#         break

def hit():
    while True:
        player1_hand.append(next(cards))
        #total up and show value
        print(player1_hand)
        #print(player1_value)


# def playagain():
#     print('Do you want to play again? (yes or no)')
#     return input().startswith('y')


##### START MAIN FUNCTION #####

print("Welcome to Blackjack, let's play! ")
cards = get_deck()
#player1_value = total()
player1_hand = []
dealer_hand = []
#### Give out two cards to player1 and one to dealer ####

print("Your hand: ")
player1_hand.append(next(cards))
player1_hand.append(next(cards))
print(player1_hand)
player1_score = score(player1_hand)
print(player1_score)

print("Dealer's hand: ")
dealer_hand.append(next(cards))
print(dealer_hand)

##playagain()