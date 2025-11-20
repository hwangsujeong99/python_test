# Dictionary = Key(이름표) 와 Value(값)
# 단어(Key) : apple / 뜻(value) : 사과

user = {

    "name" : "Kim",
    "age" : 20,
    "email" : "Kim@example.com"
}

상품 = {
 "이름" : "무선 이어폰",
 "가격" : 11111,
 "카테고리" : "전자제품"

}

user2 = dict(name = "Lee", age=25, email="asdf@dfsf.com")
empty_dict = {}

# 값 가져오기
print(user["name"])

print()
print(user.get("name"))
print(user.get("phone")) #없는 요소를 요청해도 에러가 나지 않음

#print(user["phone"]) # KeyError 발생
print(user.get("phone", "없음")) # get 방식을 권장

# 모든 키 출력
print(user.keys())

# 모든 값 출력
print(user. values())

# 모든 키-값 출력
print(user.items())

######################

# 값 추가/수정

user["city"] = "Seoul"
print(user)

# 값 삭제
del user["city"]
print(user)

# 값 꺼내기(삭제+리턴)
age11 = user.pop("age")
print(age11)
print(user)

# 전체 삭제
user.clear()
print(user)


#중첩 딕셔너리(딕셔너리 안의 딕셔너리)

users = {
    "user1":{

        "name":"Kim",
        "age" : 20
    },
    "user2":{
        "name": "Lee",
        "age": 22
    }
}

print(users["user1"]["name"])
print(users["user2"]["age"])


print()

user = {}

# 2. 정보 추가
user["name"] = "Kim"
user["age"] = 22
user["city"] = "Seoul"

print(user)
print("이름: " + user["name"])
# print("나이: " + user["age"] + "세")
# 문자열과 문자열을 연결해주는 것은 허용
# 문자열과 숫자를 직접적으로 연결해주는 것은 허용X

print("나이: " + str(user["age"]) + "세")

# f-string

print(f"이름: {user['name']}")
print(f"나이: {user['age']}세")

####

book = {

    "title" : "점프 투 파이썬",
    "price" : 10000,
    "page" : 100
}

# 1. 책 제목, 가격 출력
print(f"책 제목은 {book['title']}, 가격은 {book['price']}")

# 2. 가격을 20000원으로 변경
book["price"] = 20000
print(book)

# 3. publisher 정보 추가 : 이지스퍼블리싱
book["publisher"] = "이지스퍼블리싱"

# 4. 전체 정보 출력
print(book)

print("______ 집합 배우기 _______")
# 집합(Set) = 중복 없는 데이터 모음
fruits = {"사과", "바나나", "포도"}
numbers = {1, 2, 2, 2, 3, 4, 5}

empty_set = set() # 빈 집합 만들기

print(numbers) # 1. 중복 제거
print(fruits) # 2. 순서 없음, 출력할 때마다 다른 순서로 출력
# print(fruits[0]) # 순서가 없어서 오류가 남

print( 3 in numbers) #집합은 값을 주소로 변환해서 해시테이블로 저장
# 즉 빠르게 찾는다
# list는 처음부터 끝까지 전부 순회, 내가 찾고자하는 값이 있는지 확인

numbers = [1, 2,3, 3, 3, 3,4]
print(numbers)
# 집합으로 변환 -> 중복 제거
unique_numbers = list(set(numbers))
print(unique_numbers)

