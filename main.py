import random

def generate_initial_player_state():
    player_state = random.randint(1, 9)
    return player_state

def generate_choices(player_state, difficulty_of_choices, difficulty_delta, multiplier_range):
    multiplier = random.randint(1, multiplier_range)
    answer = player_state * multiplier
    addend = answer - player_state
    return (('*', multiplier), '+', addend)

if __name__ == "__main__":
    player_state = generate_initial_player_state()
    difficulty_of_choices = 10
    difficulty_delta = 0
    multiplier_range = 10
    choices = generate_choices(player_state, difficulty_of_choices, difficulty_delta, multiplier_range)
    print(player_state, choices)