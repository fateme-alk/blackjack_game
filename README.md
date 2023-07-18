# blackjack_game
Blackjack is a popular card game played in casinos around the world. The objective of the game is to beat
the dealer by getting a hand with a value closer to 21 than the dealer's hand, without exceeding 21.

## installation
1. Clone the repo
```
git clone https://github.com/fateme-alk/blackjack_game.git
```
2. Run the python script
```
python blackjack_game.py
```
## Usage
It's just for fun :)

## How to play
1. The game begins with the player placing a bet. Each player have enter bet amount in terminal.
2. The dealer deals two cards to each player, including themselves. Both player cards are usually face-
up, while one of the dealer's cards remains face-down .
3. Each card has a value: numbered cards are worth their face value, face cards (Jack, Queen, King)
are worth 10, and an Ace can be worth either 1 or 11, depending on the player's choice.
4. The player takes turns deciding whether to "hit" (receive another card) or "stand" (keep the
current hand).
5. The player can continue hitting until they decide to stand or until their hand exceeds 21, resulting
in a "bust" and automatic loss.
6. Once the player stands, it's the dealer's turn. The dealer reveals their face-down card and
continues drawing cards until their hand value reaches at least 17.
7. If the dealer busts, all remaining players win. Otherwise, the dealer compares their hand to each
player's hand, and the player with a higher hand value wins. In case of a tie, it's a push (a tie), and
the player keeps their bet.
8. Winnings are paid out based on the outcome of the game. Typically, a player wins 1:1 for a regular
win, 3:2 for a natural blackjack (an Ace and a 10-value card), and loses their bet if they bust or
have a lower hand value than the dealer.
### Features
- This implementation of Blackjack allows you to play the game in a command line interface.
- It follows the standard rules of Blackjack, including hitting, standing, and doubling down.
- The game keeps track of the player's balance and allows betting.
- The dealer follows a basic strategy for making decisions.
- Each hand's outcome is displayed, and the player's balance is updated accordingly
