fruits = ["사과", "바나나", "포도"]
index = 0

# while - 정확한 횟수를 모를 때
while index < len(fruits):
    print(fruits[index])
    index += 1

# for문 사용 - 리스트나 딕셔너리 사용할 때

for fruit in fruits : #fruits에서 꺼내서 fruit에 담음
    print(fruit)

# range() : 숫자 범위 만들기
for i in range(5): # 0부터 끝-1까지 (나 뺴고)
    print(i)

print("____")
for i in range(1,6): # 시작부터 끝-1까지
    print(i)

print("____")
# 시작, 끝, 증가값 : 증가값만큼 건너뛰기
for i in range(0, 10, 2): 
    print(i)

# 딕셔너리
print("__딕셔너리 : 키-값 쌍__")
user = {"name": "kim", "age" : 30}
for key, value in user.items():
    print(f"{key}: {value}")

print("__키만 필요함__")
print()
for key in user:
    print(key)

print("__값만 필요함__")
for value in user.values():
    print(value)

# 구구단 만들기
dan = int(input("몇 단을 출력할까요?"))

for i in range(1, 10):
    result = dan * 1
    print(f"{dan} x {i} = {result}")

# 2단부터 9단까지 전부 출력
## 힌트 : for문에 for문을 넣을 수 있음

