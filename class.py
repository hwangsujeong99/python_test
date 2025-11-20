# 붕어빵 틀(클래스): 설계도, 같은 모양의 붕어빵을 계속 만들 수 있음
# 실제 붕어빵(객체) : 틀로 찍어낸 결과물, 각각은 개별의 붕어빵

class Dog: # 첫글자는 대문자
    def __init__(self, name, age): # self - 자기 자신, init - 생성자
        self.name = name
        self.age  = age

    def bark(self): # 메서드의 첫 번째 매개변수는 항상 자신
        print(f"{self.name}: 멍멍 ~ ")

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}세")

# 객체 생성(붕어빵 찍어내기)
dog1 = Dog("바둑이", 3)
dog2 = Dog("초코", 5) # dog2.name 초코, dog2.age 5

# 메서드 호출 (클래스 안의 함수)
dog1.bark()
dog1.info()
print()
dog2.bark()
dog2.info()

# 강아지 클래스
class Dog:                      #클래스 = 설계도
    def __init__(self, name):
        self.name = name
        self.energy = 100

    def brak(self) : # 10씩 감소
        print("f {self.name}: 멍멍 ~~~ ")
        self.energy -= 10
    def eat(self):
        print(f"{self.name}이(가) 밥을 먹었습니다.")
        self.energy += 5

    def status(self):
        print(f"{self.name}의 에너지: {self.energy}")

my_dog = Dog("흰둥이") #객체 = 실제로 만든 것

###객체 사용
print("내 사랑 흰둥이")
my_dog.status()
my_dog.brak()
my_dog.brak()
my_dog.brak()
my_dog.status()
my_dog.eat()
my_dog.eat()
my_dog.eat()
my_dog.status()
