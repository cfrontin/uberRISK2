
import random;

import cards;

N_players= 0;
player_ids= [];
player_names= {};
player_emails= {};
player_hands= {}; # dict by player

deck= cards.deck.copy();

N_players= int(input("Enter the number of players: "));

assert(input("\nGot it. Just to be sure, you said %d players, right? (Y/N) " \
        % N_players).lower() == "y");
print();

print("Ok, now let's enter player details:\n");

for i in range(N_players):

    print("Player %d:" % i)

    # generate a player ID
    pl_id= i;

    # get input: player names
    pl_name= input("\tname: ");
    pl_email= input("\temail: ");

    # create dicts to player IDs
    player_names[pl_id]= pl_name;
    player_emails[pl_id]= player_emails;
    player_hands[pl_id]= []; # empty list of cards

    print();

print("Ok now let's flip through the deck!\n");

# shuffle the deck
random.shuffle(deck);

# # loop over the cards
# for card in deck:
#     # print("\tid: %2d" % card['id']);
#     print("\tid: %2d\t\ttype: %9s\t\tterritory: %s" % (card['id'], card['type'],
#             card['territory']));

def draw_card(deck):

    # shuffle then draw a card
    random.shuffle(deck);
    card= deck.pop();

    return card;

def exchange_cards(deck, player_hand, cards_to_exchange):
    print("not implemented!");

while len(deck) > 0:

    print("the players are:");
    for i in range(N_players):
        print("\t%2d.\t\t%s" % (i + 1, player_names[i],));
    print();
    pl_id= int(input("the player to draw (or exchange): ")) - 1;

    if pl_id >= N_players or pl_id < 0:
        print("\nthat's not a valid player!!! try again...\n");
        continue;

    action_key= input("\nok, %s press x to exchange, or d to draw: " \
            % player_names[pl_id]).lower();

    # want to do an exchange
    if action_key == 'x':
        cards_to_exchange= [];

        while len(cards_to_exchange) < 3:

            card_id= input("enter card ID to exchange (or x to quit): ");
            if card_id == 'x':
                cards_to_exchange= None;
                break;
            else:
                card_id= int(card_id);

            if card_id not in \
                    [hand['id'] for hand in player_hands[pl_id]]:
                print("\nthat's not a card in %s's hand!!! try again...\n" \
                        % player_names[pl_id]);
                print("player_hands[pl_id]");
                print(player_hands[pl_id]);
                continue;

            assert card_id not in [card['id'] for card in deck];

            card= None;
            for tmpcard in player_hands[pl_id]:
                if tmpcard['id'] == card_id:
                    card= tmpcard;
                    break;

            assert card is not None;

            cards_to_exchange.append(card);

        if cards_to_exchange is None:
            print("\nyou have bailed out of your exchange!\n");
            continue;
        else:
            # a place to store types for checking to see if exchange is valid
            exchange_types= [];

            # for each card to be exchanged
            for card in cards_to_exchange:

                # stash the important info
                if card['type'] == 'wild':
                    exchange_types += cards.card_types;
                else:
                    exchange_types.append(card['type']);
                    print(exchange_types);

            go_for_exchange= False;

            if len((set(exchange_types))) == 3:
                go_for_exchange= True;
            else:
                for unique_type in list(set(exchange_types)):
                    print("type %s, count %d" % (unique_type, exchange_types.count(unique_type)));
                    if exchange_types.count(unique_type) >= 3:
                        go_for_exchange= True;
                        break;

            if not go_for_exchange:
                print("\nthat doesn't appear to be a valid exchange. " \
                        + "try again...\n");
                continue;


            # for each card to be exchanged
            for card in cards_to_exchange:

                # pull the card out of the player's hand and put it in discard
                print("pl_id: %d" % pl_id);
                print("player_hands");
                print(player_hands);
                print("card");
                print(card);
                player_hands[pl_id].remove(card);
                deck.append(card);
                random.shuffle(deck);

    # want to draw a card
    elif action_key == 'd':

        # draw it from the deck
        card= draw_card(deck);

        # DEBUG!!!!!
        print("\tid: %2d\t\ttype: %9s\t\tterritory: %s" % (card['id'], card['type'],
                card['territory']));

        # and add it to the correct player's hand
        player_hands[pl_id].append(card);

        # DEBUG!!!!!
        print("\ndebugging sizes:");
        print("\tdeck: %d" % len(deck));
        for i in range(N_players):
            print("\tplayer %d hand: %d" % (i, len(player_hands[i])));

        print("\n");

    else:
        print("\nthat's not a valid action!!! try again...\n");
        continue;
