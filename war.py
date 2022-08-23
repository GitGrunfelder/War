from random import shuffle


class Card:
    suits = ("clubs",
             "hearts",
             "diamonds",
             "spades")
    
    values = (None, None, "2", "3",
              "4", "5", "6", "7",
              "8", "9", "10", "Jack",
              "Queen", "King", "Ace")
    
    # Card object has a value and a suit (both integers)
    def __init__(self, v, s): # These values are assigned in the deck function
        self.value = v
        self.suit = s
        
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False
    
    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False
    
    def __repr__(self):
        v = self.values[self.value] + " of " \
            + self.suits[self.suit]
        return v
    
    
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15): # For each value in outer list,
            for j in range(4): # Iterate through each suit
                self.cards.append(Card(i,j)) # and append to list cards.
        shuffle(self.cards) # Shuffle list in place.
        
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()
    
    
class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck() # Creating a deck from the Deck function.
        self.p1 = Player(name1) # Creating a player object from name1 input prompt.
        self.p2 = Player(name2)
        
    def wins(self, winner):
        w = f"{winner} wins this round"
        print(w)
        
    def draw(self, p1n, p1c, p2n, p2c):
        d = f"{p1n} drew {p1c} {p2n} drew {p2c}"
        print(d)
        
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name, p1.wins
        if p1.wins < p2.wins:
            return p2.name, p2.wins
        return "It was a tie!"
   
    def play_game(self):
        cards = self.deck.cards # This is assigning a shuffled deck to the cards variable.
        print("beginning War!")
        while len(cards) >= 2: # While at least 2 cards remain
            m = "q to quit. Any " + "key to play:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card() # Remove a card from the shuffled cards list, assign to p1
            p2c = self.deck.rm_card()
            p1n = self.p1.name # Assign p1 name to p1n
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c) # Tells what each player drew
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name) # Prints win message, using this name as winner variable.
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        
        win = self.winner(self.p1, self.p2) # Assigns name with most wins to win variable via winner function.
        final_score = f"Final score: {self.p1.name}:{self.p1.wins} {self.p2.name}:{self.p2.wins} "
        # This is printed when either cards < 2 or input is q.
        print(f"War is over. {win[0]} wins with a score of {win[1]} wins!") # Name from win is declared winner! 
        print(final_score)
        

        
    
game = Game()
game.play_game()


# I would like to iterate this project, by adding an alternate mode, where rather than suits being considered,
# it would play like how I have always played.
# If you both place the same value, regardless of suit, you enter a war :
# Both users place 3 cards face down and a final card on top, whichever is higher takes the stack.
# Once all cards are gone, users count their total cards (gotten via winning each round with a higher value)
# This would be a good use of branching, and a good point to dip my toes in.
        
    