import random
import csv

def generate_pool():
    player_states = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    pool = {}
    for i in range(1, 16):
        pool[i] = []
    index = 0
    for i in range(1, 16):
        for j in range(15):
            pool[i].append(player_states[index % 9])
            index += 1
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
    if random.choice([True, False]) or addend - difficulty_of_choices <= 0:
        addend += difficulty_of_choices
    else:
        addend -= difficulty_of_choices

    # 선택지의 순서를 섞음
    if random.choice([True, False]):
        return (('*', multiplier), ('+', addend))
    else:
        return (('+', addend), ('*', multiplier))

def choice_to_str(choice):
    operator = choice[0]
    operand = str(choice[1])
    result = "x" if operator == "*" else "+"
    result += operand
    return result

def calculate_answer(player_state, choices):
    first_operator = choices[0][0]
    first_operand = choices[0][1]
    second_operator = choices[1][0]
    second_operand = choices[1][1]

    first_result = 0
    if first_operator == "*":
        first_result = player_state * first_operand
    else:
        first_result = player_state + first_operand

    second_result = 0
    if second_operator == "*":
        second_result = player_state * second_operand
    else:
        second_result = player_state + second_operand

    if first_result > second_result:
        return "left"
    else:
        return "right"

def generate_csv_from_pool(pool):
    csvfile = open("choicies.csv", "w")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["index",
                        "left",
                        "right",
                        "player_state",
                        "difficulty_of_choices",
                        "answer",
                        "round",
                        "set"])
    index_ = 1;
    round_ = 1;
    set_ = 1;
    for j in range(15):
        for difficulty_of_choices in range(1, 16):
            player_state = pool[difficulty_of_choices][j]
            choice = generate_choices(player_state, difficulty_of_choices, multiplier_range=9)
            answer = calculate_answer(player_state, choice)
            csvwriter.writerow([index_,
                                choice_to_str(choice[0]),
                                choice_to_str(choice[1]),
                                player_state,
                                difficulty_of_choices,
                                answer,
                                str(round_) + "-" + str(set_),
                                (index_ - 1) % 15 + 1])
            index_ += 1
            if (index_ - 1) % 15 == 0:
                set_ += 1
            if set_ == 6:
                round_ += 1
                set_ = 1
    csvfile.close()

if __name__ == "__main__":
    pool = generate_pool()
    print_pool(pool)
    generate_csv_from_pool(pool)
