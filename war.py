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
    def __init__(self, v, s):
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
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        
        win = self.winner(self.p1, self.p2)
        
        print(f"War is over. {win} wins!")
        
    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"
        
    

    
    
game = Game()
game.play_game()
        
    