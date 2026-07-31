import art
import random
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def compare_hands():
    if sum(player_cards) == sum(computer_cards):
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("It's a draw.")
    elif sum(player_cards) > 21:
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("You went over. You lose 😭")
    elif sum(computer_cards) > 21:
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("Opponent went over. You win 😁")
    elif sum(player_cards) > sum(computer_cards):
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("You win 😃")
    elif sum(player_cards) < sum(computer_cards):
        print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
        print("You lose 😤")
def show_cards():
    print(f"Your cards: {player_cards}, current score {sum(player_cards)}")
    print(f"Computer's first card : {computer_cards[0]}")
def double_ace(hand):
    if hand == [11, 11]:
        y = hand.index(11)
        hand[y] = 1
def natural_blackjack(player, computer):
    if sum(player) == 21 or sum(computer) == 21:
        if sum(player) == 21 and sum(computer) == 21:
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("It's a draw.")
        elif sum(player) == 21:
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("You win 😃")
        elif sum(computer) == 21:
            print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
            print(f"Computer's final hand: {computer_cards}, final score: {sum(computer_cards)}")
            print("You lose 😤")
        return True
    return False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_continue = True
while should_continue:
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if choice == "y":
        clear()
        print(art.logo)
        player_cards = random.choices(cards, k = 2)
        computer_cards = random.choices(cards, k = 2)
        double_ace(computer_cards)
        double_ace(player_cards)
        if natural_blackjack(player_cards, computer_cards):
            continue
        show_cards()
        choice1 = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice1 == "y":
            while choice1 == "y":
                player_cards.append(random.choice(cards))
                if sum(player_cards) > 21 and 11 in player_cards:
                    x = player_cards.index(11)
                    player_cards[x] = 1
                if sum(player_cards) >= 21:
                    choice1 = "n"
                else:
                    show_cards()
                    choice1 = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))
            if sum(computer_cards) > 21 and 11 in computer_cards:
                x = computer_cards.index(11)
                computer_cards[x] = 1
        compare_hands()
    else:
        should_continue = False