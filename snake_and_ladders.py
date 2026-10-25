import random

def play_game():
    # Ladders map the bottom square to the top destination square
    ladders = {
        1: 38,
        4: 14,
        9: 31,
        21: 42,
        38: 84,
        51: 67,
        72: 91,
        80: 99
    }
    
    # Snakes map the head square to the tail destination square
    snakes = {
        17: 7,
        54: 34,
        62: 19,
        64: 60,
        87: 36,
        93: 73,
        95: 75,
        98: 79
    }
    
    # Player initialization
    player_positions = [0, 0]
    player_names = ["Player 1", "Player 2"]
    turn = 0
    
    print("=" * 35)
    print("   WELCOME TO SNAKES & LADDERS   ")
    print("=" * 35)
    print("Rules: Exact roll needed to hit 100 to win!")
    
    while True:
        current_player = player_names[turn]#0 means player1 1 means player 2
        current_pos = player_positions[turn]
        
        # Wait for user input to simulate a dice roll
        input(f"\n[{current_player}] Press Enter to roll the dice...")
        

        dice = random.randint(1, 6)
        print(f"{current_player} rolled a {dice}")
        
        new_pos = current_pos + dice #3+2=5
        
        # Rule: Must land exactly on 100 to win
        if new_pos > 100:#current=97 dice=5 97+5=102
            print(f"Roll too high! {current_player} stays at square {current_pos}")
        else:#c=97 d=2 97+2=99
            print(f"Moving from {current_pos} to {new_pos}")
            
            # Check for Ladders
            if new_pos in ladders:#c=3 d=1 n=3+1=4 l_p=14
                print(f"Awesome! A ladder! Climbing up from {new_pos} to {ladders[new_pos]}")
                new_pos = ladders[new_pos]
                
            # Check for Snakes
            if new_pos in snakes:#c=15 d=2 n=17s_p=7
                print(f"Oh no! A snake bit you! Sliding down from {new_pos} to {snakes[new_pos]}")
                new_pos = snakes[new_pos]
                
            player_positions[turn] = new_pos
            print(f"Current Position: {current_player} is now on square {new_pos}")
            
            # Check Win condition
            if new_pos == 100:
                print("\n" + "*" * 45)
                print(f"CONGRATULATIONS! {current_player} WINS!")
                print("*" * 45)
                break
                
        # Toggle turn between 0 and 1
        turn = 1 - turn

play_game()
