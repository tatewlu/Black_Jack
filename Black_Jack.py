import random
from enum import Enum

#Variables used to control the flow of the game
game_over = False
stop = False
multi_black_jack = []
x = 1

# An enumeration used in the Card class to keep track of what suit
class suit(Enum):
    SPADE = "Spade"
    DIAMOND = "Diamond"
    CLUB = "Club"
    HEART = "Heart"

#the card class lets players have cards to draw
class Card:
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
        self.is_ace = False

    def get_value(self):
        if self.number == 1:
            val = 11
            is_ace = True
        elif (
            self.number == 10
            or self.number == 11
            or self.number == 12
            or self.number == 13
        ):
            val = 10
        else:
            val = self.number
        return val

#the function that generates cards
def generate_card():
    my_suit = random.choice(list(suit))
    my_value = random.randint(1, 13)
    return Card(my_suit, my_value)

#the player class makes players for the players to control and play with
class Player:
    def __init__(self):
        self.has_busted = False
        self.cards_held = []
        self.bank_roll = 100
        self.num_aces = 0
        self.blackjack = False

#the function that gives cards to players
    def get_card(self):
        temp_card = generate_card()
        if temp_card.is_ace == True:
            self.num_aces += 1
        self.cards_held.append(temp_card)

#lets people with aces subtract 10 if they bust
    def get_ace_effect(self):
        self.cards_held.append(Card("Spade", -10))

#scores that round
    def get_points(self):
        total = 0
        for item in self.cards_held:
            total += item.get_value()
        return total

#lets the players know the dealer's top card
    def show_top_card(self):
        # Only give value of top card until players are done
        print(self.cards_held[0].get_value())

#shows the dealer's cards to everyone
    def show_cards(self):
        total = 0
        for item in self.cards_held:
            print(item.get_value())

def begin():
    dealer_array = []
    player_array = []
    print("Welcome to Black Jack")
    print(" ")
    stop = False
    winner_declared = False

#give the dealer his cards
    dealer = Player()
    dealer.get_card()
    dealer.get_card()
    dealer_array.append(dealer)


    while stop == False:
        try:
            num_people = int(input("How many people are playing? Please type in a number from the keypad. (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) "))
#catches value errors
        except ValueError:
            print("Oops! That input is not a valid number/string between 1 and 10.")
            print("If you typed in a letter, please use numbers instead of letters and symbols.")
            print(" ")
            print("Please try again.")
            print(" ")
            but = True
            break

            winner_declared = False
            print(" ")

#catches number errors
        if num_people < 1:
            winner_declared = True
            print("Dealer automatically wins because he is the only one playing")
            print(" ")
            print("New Round")
            print(" ")

#same thing
        elif num_people > 10:
            print("Too many people. Maximum number of players is 10")
            winner_declared = True
            print("")


#the real game starts here
        while winner_declared == False:
            # Initial deal 2 cards each player
            for i in range(num_people):
                temp_player = Player()
                temp_player.get_card()
                temp_player.get_card()
                player_array.append(temp_player)

            # Print everyone's hands plus dealer
            for i in range(len(player_array)):
                print("Player ", i + 1, " has: ")
                player_array[i].show_cards()
                print("Total: ", player_array[i].get_points())
                print(" ")

            dealing_end = True
            print("Dealer is showing: ")
            dealer.show_top_card()
            print(" ")

            # Players must decide to hit or stay
            for i in range(len(player_array)):
                hit = 0
                print("Player ", i + 1, ", do you want to hit or stay?")
                hit = int(input("Enter 1 for hit and 0 for stay: "))
                while hit == 1:
                    player_array[i].get_card()
                    print("Player ", i + 1, " has: ")
                    player_array[i].show_cards()
                    print("Total: ", player_array[i].get_points())
                    if player_array[i].get_points() > 21:
                        if player_array[i].num_aces == 1:
                            player_array[i].get_ace_effect()
                        elif player_array[i].num_aces == 2:
                            player_array[i].get_ace_effect()
                        elif player_array[i].num_aces == 3:
                            player_array[i].get_ace_effect()
                        elif player_array[i].num_aces == 4:
                            player_array[i].get_ace_effect()
                        else:
                            player_array[i].has_busted = True
                            print("Player ", i + 1, "busts!")
                            break
                    elif player_array[i].get_points() == 21:
                        print("Player ", i+1, " got black jack!")
                        player.blackjack = True


                    print("Player ", i + 1, ", do you want to hit or stay?")
                    print("Player ", i + 1, "")
                    hit = int(input("Enter 1 for hit and 0 for stay: "))

            # All players have stayed or busted, dealer's turn
            dealer.show_cards()
            print("Dealer has:", dealer_array[i].get_points())
            # If dealer has less than 17, they must hit
            while dealer.get_points() < 17:
                dealer.get_card()
                print("Dealer has :", dealer_array[i].get_points())
                dealer.show_cards()
                if dealer.get_points() > 21:
                    if dealer.num_aces > 0:
                        dealer.append(get_ace_effect)
                        dealer.num_aces -= 1
                    else:
                        dealer.has_busted = True
                        print("Dealer busts!")
                        winner_declared = True
                        break

            # If we haven't broken from the while loop, it's time to determine who beat the dealer
            for i in range(len(player_array)):
                if dealer.has_busted == True:
                    if player_array[i].has_busted == True:
                        print("Player ", i + 1, " beat the dealer!")
                elif dealer.get_points() < player_array[i].get_points():
                    if player_array[i].has_busted == False:
                        print("Player ", i + 1, " beat the dealer!")
                    else:
                        print("Player ", i + 1, " lost!")
                elif dealer.get_points() == player_array[i].get_points():
                    if player_array[i].has_busted == False:
                        print("Player ", i + 1, " pushes!")
                    else:
                        print("Player ", i + 1, " lost!")
                else:
                    print("Player ", i + 1, " lost!")
            winner_declared = True
            dealer.cards_held.clear()
            dealer.get_card()
            dealer.get_card()
            dealer.has_busted = False
            player_array.clear()
            dealer_array.clear()
            print(" ")
            print("Program over.")
            print("Please run the code again to play again.")
            print(" ")
            stop = True


def deal_players(people):
    #    players
    # account for the dealer
    for i in range(people + 1):
        print("Player ", i, "has cards ")


#infinite playing loop
begin()
#future work:
    #tracking black jacks
    #not letting people draw on 21
    #making aces better
    #making it one deck
    #making variants

