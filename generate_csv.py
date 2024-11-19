import random
import csv

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

def generate_csv_from_pool(pool):
    csvfile = open("choicies.csv", "w")
    csvwriter = csv.writer(csvfile)
    index_ = 1;
    round_ = 1;
    set_ = 1;
    for difficulty_of_choices, v in pool.items():
        for player_state in v:
            choice = generate_choices(player_state, difficulty_of_choices, multiplier_range=9)
            csvwriter.writerow([index_, player_state, difficulty_of_choices, round_, set_])

            index_ += 1
            set_ += 1
            if set_ == 6:
                round_ += 1
                set_ = 1
    csvfile.close()

if __name__ == "__main__":
    pool = generate_pool()
    print_pool(pool)
    generate_csv_from_pool(pool)
