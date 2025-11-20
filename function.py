'''
# 첫 번째 계산
a = 10
b = 5
result1 = a + b
print(f"{a} + {b} = {result1}")

# 두 번째 계산
a = 20
b = 9
result2 = a + b
print(f"{a} + {b} = {result2}")

print("---- 함수 -----")
## 함수 정의
def add(a, b): ##매개변수 - 입력받을 값
    result = a + b
    print(f"{a} + {b} = {result}")

add(10, 5) ## 함수 호출
add(20, 7)

def say_hello():
    print("안녕하세요")

say_hello() #이제 실행!

# 매개 변수(parameter) : 함수에 정보 전달
def great(name):
    print(f"안녕하세요, {name}님. ")

great("user01")
great("user02")

# 여러 개의 매개변수
def introduce(name, age):
    print(f"이름: {name} ")
    print(f"나이: {age}세")

introduce("KIM", 22)

# return : 함수가 값을 돌려주기
def add(a, b):
    return a + b

result = add(10, 5)
print(result)
print(result * 2)
'''

# print VS return

def add_print(a, b):
    print(a + b)
def add_return(a, b):
    return(a + b)

print("print VS return")
x = add_print(10, 5) # x에는 담긴 게 없음
print(x)
# print(x * 2) # 에러 ! None은 곱셈 안됨

print("return!!!!!!!!!!")
y = add_return(10, 5)
print(y)
print(y - 2)