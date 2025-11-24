# Python Based Blackjack Game

Python terminal based Blackjack game under 1 hour.

## Planning

### Rules of the game
* This is a card game
* You play with a full deck of cards
* Goal is to hit 21
* If a player exceeds 21, they lose the game
* You play against the dealer
* Each player starts with 2 cards up, dealer starts with 1 card up 1 card down
* At each turn the player can choose to get a new card (hit) or end the turn (stand)
* After all players are done, the dealer shows the hand and draws a card until total is >= 17
* After the dealer is ok, total points are compared. Closer to 21 wins. There could also be a tie.
* 2 to 10 are counted as 10. J, Q, K are 10. A could be either 11 or 1.
* A + J, Q, K are considered natural blackjack and it automatically wins unles both dealer and the player has it which means a tie.

### User goals
* Have a fun and realistic Blackjack experience
* Play again
* See scores
* See my hand properly
* etc.

### Developer goals
* Practice Python
* Experiment with Python fucntions and classes
* Showcase my Python skills in a public repository
* etc.

### Features to implement
* Card deck management (create, shuffle, draw, discard)
* Score management and calculation
* Player (human) interaction
* Dealer AI

### Features left to implement in the future
* At the moment, the app uses 1 deck of cards. In the future make it
flexible.

### UX and Design
* This is a terminal based game, we won't use fancy graphics
* Print statements are fine

It can look like this:
```
Dealer's hand: A, ?
Player's hand: 4, 7, 8

> What's your choice (h)it or (s)tand?
```
