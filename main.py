import random

def generate_initial_player_state():
    player_state = random.randint(1, 9)
    return player_state

def generate_choices(player_state, difficulty_of_choices, difficulty_delta, multiplier_range):
    # 곱하기 연산자의 오른쪽 피연산자 생성
    multiplier = random.randint(1, multiplier_range)
    # 곱하기 연산 했을 때 정답 계산
    answer = player_state * multiplier
    # 정답에서 역산하여 더하기 연산자의 오른쪽 피연산자 계산
    addend = answer - player_state

    # difficulty_of_choices에 변동 추가
    delta = random.randint(-difficulty_delta, difficulty_delta)
    adjusted_difficulty = difficulty_of_choices + delta
    print(adjusted_difficulty)

    # 절반의 확률로 addend에서 difficulty_of_choices를 더하거나 뺌
    if random.choice([True, False]):
        addend += adjusted_difficulty
    else:
        addend -= adjusted_difficulty

    if random.choice([True, False]):
        return (('*', multiplier), ('+', addend))
    else:
        return (('+', addend), ('*', multiplier))

if __name__ == "__main__":
    DIFFICULTY_OF_CHOICES = 5
    DIFFICULTY_DELTA = 1
    MULTIPLIER_RANGE = 10

    player_state = generate_initial_player_state()

    choices = generate_choices(player_state, DIFFICULTY_OF_CHOICES, DIFFICULTY_DELTA, MULTIPLIER_RANGE)
    print(player_state, choices)