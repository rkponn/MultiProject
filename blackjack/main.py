import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
players_hand = []
dealers_hand = []

def dealt_card():
    card = random.choice(deck)
    deck.remove(card)
    return card

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2 and 11 in hand:
        return 0
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def deal_cards():
    for _ in range(2):
        players_hand.append(dealt_card())
        dealers_hand.append(dealt_card())

def compare_scores(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"
    if player_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

if __name__ == "__main__":
    deal_cards()
    game_over = False

    while not game_over:
        player_score = calculate_score(players_hand)
        dealer_score = calculate_score(dealers_hand)
        print(f"Your cards: {players_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealers_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            user_should_continue = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_continue == 'y':
                players_hand.append(dealt_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealers_hand.append(dealt_card())
        dealer_score = calculate_score(dealers_hand)

    print(f"Your final hand: {players_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealers_hand}, final score: {dealer_score}")
    print(compare_scores(player_score, dealer_score))