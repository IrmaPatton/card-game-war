from random import shuffle


def greeting_rules():
    print('''Welcome to Virtual Card Games: War
Choose your player see who wins.
''')


def card_shuffle():  #shuffles the deck
    card_deck = [
        13, 12, 11, 14, 10, 9, 8, 7, 6, 5, 4, 3, 2, 13, 12, 11, 14, 10, 9, 8,
        7, 6, 5, 4, 3, 2, 13, 12, 11, 14, 10, 9, 8, 7, 6, 5, 4, 3, 2, 13, 12,
        11, 14, 10, 9, 8, 7, 6, 5, 4, 3, 2
    ]  # 11=J 12=Q 13=K 14=A
    shuffle(card_deck)
    return card_deck


def split_the_deck(card_deck):  #makes the deck two hands for players
    player_one_deck = card_deck[:26]
    player_two_deck = card_deck[26:]
    return player_one_deck, player_two_deck


def check_pop(player_one_deck, player_two_deck, player_1_pile, player_2_pile):
    #if decks is empty
    if player_one_deck == []:
        player_one_deck.extend(player_1_pile)  #checks if empty and adds pile
        player_1_pile.clear()
    if player_two_deck == []:
        player_two_deck.extend(player_2_pile)
        player_2_pile.clear()
    #if decks is still empty after that
    if player_one_deck == []:
        print('''
Player2 wins war.''')
        exit()
    if player_two_deck == []:
        print('''
Player1 wins war.''')
        exit()


def play_time(player_one_deck, player_two_deck):  #plays war
    #gets decks and piles ready to play
    player_1_pile = []
    player_2_pile = []
    battle_casualties = []
    print('''I Mr. Computer am ready.
Place your bets on Player1 or Player2.
It's time for war.''')
    round_count = 0  #
    #now plays war
    while True:
        round_count += 1
        print('Rounds played: ', round_count)

        #if decks is not empty
        check_pop(player_one_deck, player_two_deck, player_1_pile,
                  player_2_pile)
        P1_hit = player_one_deck.pop()  #sometimes pops a empty list?
        check_pop(player_one_deck, player_two_deck, player_1_pile,
                  player_2_pile)
        P2_hit = player_two_deck.pop()
        if P1_hit > P2_hit:
            player_1_pile.append(P1_hit)
            player_1_pile.append(P2_hit)
            player_1_pile.extend(battle_casualties)
            battle_casualties.clear()
            print('''
Player1 won!''')
        elif P2_hit > P1_hit:
            player_2_pile.append(P1_hit)
            player_2_pile.append(P2_hit)
            player_2_pile.extend(battle_casualties)
            battle_casualties.clear()
            print('''
Player2 won!''')
        else:  #if cards == each other(battle)
            print('Tie:', P1_hit, P2_hit)
            battle_casualties.append(P1_hit)
            battle_casualties.append(P2_hit)
            for _ in range(3):
                check_pop(player_one_deck, player_two_deck, player_1_pile,
                          player_2_pile)
                battle_casualties.append(player_one_deck.pop())

            for _ in range(3):
                check_pop(player_one_deck, player_two_deck, player_1_pile,
                          player_2_pile)
                battle_casualties.append(player_two_deck.pop())
                #sometimes pops a empty list?


def main():
    greeting_rules()
    card_deck = card_shuffle()
    player_one_deck, player_two_deck = split_the_deck(card_deck)
    play_time(player_one_deck, player_two_deck)


if __name__ == '__main__':
    main()
