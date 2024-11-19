import random
import time

def generate_pool():
    pool = {}
    for i in range(1, 16):
        pool[i] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    state = 1
    count = 0
    for j in range(6):
        for i in range(1, 16):
            pool[i].append(state)
            count += 1
            if count % 10 == 0:
                state += 1
    return pool

def print_pool(pool):
    for k, v in pool.items():
        print(k, end="\t")
        for e in v:
            print(e, end=", ")
        print()

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
    choices_pool = generate_pool()
    print_pool(choices_pool)
