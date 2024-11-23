import random
import time

def generate_initial_player_state():
    # 플레이어의 상태를 1의 자리수 수 중 랜덤으로 설정
    player_state = random.randint(1, 9)
    return player_state

def generate_choices(player_state, difficulty_of_choices, multiplier_range=9):
    # 곱하기 연산자의 오른쪽 피연산자 생성
    multiplier = random.randint(1, multiplier_range)
    # 곱하기 연산 했을 때 정답 계산
    answer = player_state * multiplier
    # 정답에서 역산하여 더하기 연산자의 오른쪽 피연산자 계산
    addend = answer - player_state

    # 절반의 확률로 addend에서 difficulty_of_choices를 더하거나 뺌
    if random.choice([True, False]) or player_state + (addend - difficulty_of_choices) <= 0:
        addend += difficulty_of_choices
    else:
        addend -= difficulty_of_choices

    # 선택지의 순서를 섞음
    if random.choice([True, False]):
        return (('*', multiplier), ('+', addend))
    else:
        return (('+', addend), ('*', multiplier))

def print_choices(choices):
    first_operator = choices[0][0]
    first_operand = str(choices[0][1])
    second_operator = choices[1][0]
    second_operand = str(choices[1][1])

    print("choices:\t", end="")
    print(first_operator + first_operand, end="")
    print(" / ", end="")
    print(second_operator + second_operand)


if __name__ == "__main__":
    DIFFICULTY_OF_CHOICES = 5

    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)
    print()

    while True:
        player_state = generate_initial_player_state()
        choices = generate_choices(player_state, DIFFICULTY_OF_CHOICES)

        print("player_state:", player_state, sep='\t')
        print_choices(choices)
        print()

        time.sleep(2)
