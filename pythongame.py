import random

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.is_alive = True
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False
    
    def heal(self, amount):
        self.health = min(100, self.health + amount)
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
    
    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Inventory:")
            for item in self.inventory:
                print("-", item)

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.is_alive = True
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_alive = False

class Game:
    def __init__(self):
        self.player = None
        self.current_enemy = None
    
    def start(self):
        print("Welcome to the Adventure Game!")
        self.player = Player(input("Enter your name: "))
        self.intro_story()
        self.game_loop()
    
    def intro_story(self):
        print(f"Hello, {self.player.name}! You find yourself in a mysterious land...")
        # Add more storyline
        
    def game_loop(self):
        while self.player.is_alive:
            self.handle_combat()
            # Other game loop actions like exploring, puzzles, etc.
    
    def handle_combat(self):
        self.current_enemy = Enemy("Orc", 50, 10)  # Example enemy
        print(f"A wild {self.current_enemy.name} appears!")
        
        while self.current_enemy.is_alive and self.player.is_alive:
            action = input("What will you do? (attack/heal/run) ").lower().strip()
            
            if action == "attack":
                self.attack_enemy()
            elif action == "heal":
                self.player.heal(20)
                print("You healed yourself.")
            elif action == "run":
                print("You managed to escape!")
                break
            else:
                print("Invalid action. Try again.")
        
    def attack_enemy(self):
        # Calculate player's attack power based on items, etc.
        player_attack_power = random.randint(5, 15)
        self.current_enemy.take_damage(player_attack_power)
        print(f"You attack the {self.current_enemy.name} for {player_attack_power} damage.")
        
        if not self.current_enemy.is_alive:
            print(f"You defeated the {self.current_enemy.name}!")
            # Add rewards, progression, etc.
        else:
            enemy_attack_power = random.randint(3, 8)
            self.player.take_damage(enemy_attack_power)
            print(f"The {self.current_enemy.name} attacks you for {enemy_attack_power} damage.")
            
            if not self.player.is_alive:
                print("Game over. You have been defeated.")
            else:
                print(f"Your health: {self.player.health}")
    
    # Additional methods for puzzles, quests, etc. can be added as needed

if __name__ == "__main__":
    game = Game()
    game.start()