import random


def draw(card):
    new_card = random.choice(card)
    return new_card


def calculate_score(hand):
    if sum(hand) > 21 and 11 in hand:
        card_swap = hand.index(11)
        hand[card_swap] = 1
    return sum(hand)


def find_winner(user_score, dealer_score):
    if user_score > dealer_score:
        print("You win!")
    elif dealer_score > user_score:
        print("Dealer won")
    elif user_score == dealer_score:
        print("It's a draw")


def blackjack():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    user_hand = []
    dealer_hand = []

    for n in range(2):
        user_hand.append(draw(cards))
        dealer_hand.append(draw(cards))

    print(f"Your hand: {user_hand} | Your score: {calculate_score(user_hand)}")
    print(f"Dealer hand: {dealer_hand[0]}")

    game_on = True
    while game_on:
        print("")
        hit = input("Press 'h' to hit. Press 's' to stand. ").lower()
        if hit == "h":
            user_hand.append(draw(cards))
            print(f"Your hand: {user_hand} | Your score: {calculate_score(user_hand)}")
            print(f"Dealer hand: {dealer_hand[0]}")
            if calculate_score(user_hand) > 21:
                print("Bust")
                game_on = False
        elif hit == "s":
            while sum(dealer_hand) < 17:
                dealer_hand.append(draw(cards))
                calculate_score(dealer_hand)
            print(f"Your hand: {user_hand} | Your score: {calculate_score(user_hand)}")
            print(f"Dealer hand: {dealer_hand} | Dealer's score: {calculate_score(dealer_hand)}")
            find_winner(calculate_score(user_hand), calculate_score(dealer_hand))
            game_on = False
    print("")
    play_again = input("Press 'y' to play again ").lower()
    if play_again == "y":
        blackjack()
    else:
        print("Thank you for playing!")


blackjack()
