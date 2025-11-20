import random

# number = random.randint(1, 100)
# print(f"랜덤 숫자: {number}")

# 게임 로직
# 1. 컴퓨터가 1 ~ 10 사이 숫자를 하나 정함
# 2. 사용자가 숫자를 입력
# 3. 컴퓨터가 힌트 제공: 높음, 낮음, 정답
# 4. 몇 번 만에 맞추는지 카운트

answer = random.randint(1, 10) # 지정된 두 수 사이(양 끝의 수도 포함)의 임의의 정수를 생성하는 함수
tries = 0

print("===== 숫자 맞추기 게임 =====")
print("1부터 10 사이의 숫자를 맞춰보세요~!")

while True:
    # 사용자 입력
    user = int(input("\n숫자를 입력하세요: "))
    tries += 1

    # 3단계 정답확인
    if user == answer:
        print(f"정답입니다! {tries}번 만에 맞추셨습니다.")
        break
    elif user < answer :
        print("더 높습니다")
    else:
        print("더 낮습니다")
        