import random

class Participant:
    def __init__(self):
        self.cards = []
        
    def get_cards(self, cards):
        card = random.choice(cards)
        self.cards.append(card)
        cards.remove(card)

class Player(Participant):
    def __init__(self, number):
        self.number = number
        self.bet_amount = None
        super().__init__()
        
    def get_bet_amount(self):
        self.bet_amount = float(input(f'{self.__class__.__name__} {self.number} enter you\'r bet amount: '))
        
    def __repr__(self):
        return f'{self.__class__.__name__}{self.number} has cards: {self.cards}'
    
class Dealer(Participant):
    def print_first_hand(self):
        return f'{self.__class__.__name__} has cards: {self.cards[0]}, hidden card'
    
    def __repr__(self):
        return f'{self.__class__.__name__} has cards: {self.cards}'
    
class Card:
    def __init__(self, symbol, value):
        self.symbol = symbol
        self.value = value
    
    def __repr__(self):
        return f'{self.symbol}: {self.value}'

def create_cards():
    cards = []
    for symbol in ('Diamond', 'Heart', 'Cube', 'Spde'):
        for value in [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']:
            cards.append(Card(symbol, value))
    return cards

def create_players():
    num_of_players = int(input('enter number of players: '))
    players = []
    for i in range(num_of_players):
        player = Player(i + 1)
        player.get_bet_amount()
        players.append(player)
    return players
    
def give_initial_cards(participants, cards):
    for i in range(1,3):
        for participant in participants.copy():
            participant.get_cards(cards)
            if i == 1:
                print(participant)
            else:
                if (participant.__class__.__name__ == 'Dealer'):
                    print(participant.print_first_hand())
                else:
                    print(participant)
                    if blackjack(participant):
                        print(f'{participant.__class__.__name__} {participant.number}, blackjack happened')
                        participants.remove(participant)
                    
def hand_value(participant):
    hand_value = 0
    num_of_aces = 0
    for card in participant.cards:
        if card.value == 'A':
            num_of_aces =+ 1
        elif card.value in ['J', 'Q', 'K']:
           hand_value += 10
        else:
            hand_value += card.value
    if num_of_aces == 1:
        if hand_value <= 10:
            hand_value += 11
        else:
            hand_value += 1
    elif num_of_aces == 2:
        if hand_value <= 9:
            hand_value += (11 + 1)
        else:
            hand_value += (num_of_aces * 1)
    elif num_of_aces == 3:
        if hand_value <= 8:
            hand_value += (11 + 1 + 1)
        else:
            hand_value += (num_of_aces * 1)
    elif num_of_aces == 4:
        if hand_value <= 7:
            hand_value += (11 + 1 + 1 + 1)
        else:
            hand_value += (num_of_aces * 1)
    return hand_value

def blackjack(participant):
    blackjack = False
    if hand_value(participant) == 21:
        blackjack = True
    return blackjack

def get_action(participant):
    action = str(input(f'{participant}, enter you\'re next action: '))
    return action

def make_decision(participant, participants, cards):
    action = get_action(participant)
    while action != 'stand':
        if action == 'hit':
            hit(participant, cards)
            if bust(participant):
                print(f'{participant.__class__.__name__} {participant.number}, bust happened')
                participants.remove(participant)
                return
            if blackjack(participant):
                print(f'{participant.__class__.__name__} {participant.number}, blackjack happened')
                participants.remove(participant)
                return
            action = get_action(participant)
            continue
        elif action == 'double':
            double(participant)
            hit(participant, cards)
            if bust(participant):
                print(f'{participant.__class__.__name__} {participant.number}, bust happened')
                participants.remove(participant)
                return
            if blackjack(participant):
                print(f'{participant.__class__.__name__} {participant.number}, blackjack happened')
                participants.remove(participant)
                return
            # we write break keyword here, because after double hand, it's next players's turn
            break
            # action = get_action(participant)
            # continue
        else:
            # would be split action
            pass
            
def bust(participant):
    bust = False
    if hand_value(participant) > 21:
        bust = True
    return bust


def hit(participant, cards):
    participant.get_cards(cards)
    print(participant)

def double(participant):
    participant.bet_amount = 2 * (participant.bet_amount)

def play_game():
    cards = create_cards()
    
    players = create_players()
    
    dealer = Dealer()
    
    participants = [player for player in players] + [dealer]
    print(participants)
    
    give_initial_cards(participants, cards)
    
    for player in players:
        make_decision(player, participants, cards)
    

    remind_players = participants[:len(participants) - 1]
    print(f'remind_players: {remind_players}')
    show_dealer_hand(dealer)
    
    finish = dealer_hand(dealer, cards)

    if finish:
        print('end of the game')
    else:
        for player in remind_players:
         compare_hands(player, dealer)


def show_dealer_hand(dealer):
    print(dealer)

def dealer_hand(dealer, cards):
    finish = False
    while hand_value(dealer) < 17:
        hit(dealer, cards)
        if bust(dealer):
            print('all players win')
            finish = True
        if blackjack(dealer):
            print('all players lose, dealer black jack')
            finish = True
    return finish 
    
    
def compare_hands(player, dealer):
    print(f'compare player {player.number} with dealer: ')
    if hand_value(player) > hand_value(dealer):
        print('player wins')
    elif hand_value(player) == hand_value(dealer):
        print('no one wins')
    else:
        print('dealer wins')
    


play_game()