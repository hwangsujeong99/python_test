'''
student1 = "일철수"
# list (목록) : 여러 개의 값을 하나로 묶은 것
# 학생 이름 목록
students = ["1철수", "2철수", "3철수", ] #마지막 콤마는 문법적 허용(해도 되고 안 해도 됨)

# 숫자 목록
scores = ["문자열", 11, 22, 33, True] # 다른 종류의 데이터 가능하지만, 추천X
print(scores)                           # 관리하기 힘듬

print("=============")
fruits = ["사과", "바나나", "메론"] # 0번지부터

print(fruits[-1])
fruits.append("귤") # 리스트의 마지막에 추가
print(fruits)

print(len(fruits)) # 리스트 길이
print("++++++++++++++")
print(fruits[-3])

print("+++++++슬라이싱++++++++")
# 슬라이싱 : 여러 개 잘라내기
# [시작:끝] -> 시작 위치부터 (끝-1) 위치까지
print(fruits[1:3])
print(fruits[0:3]) # 사과, 바나나, 멜론

print("===========리스트 수정============")
fruits = ["사과", "바나나", "포도"]
print(fruits)

# 값 변경
fruits[1] = "딸기"
print(fruits)

# 값 추가(중간에)
print()
fruits.insert(1, "망고") # 망고 뒤로 모든 게 밀림
print(fruits)

# 값 삭제
print()
del fruits[2]
print(fruits)

# 마지막 값 꺼내서(삭제 + 리턴(사용하기)) -> 삭제하기 전 한 번 더 사용하고 싶을 때
last = fruits.pop()
print(last)
print(fruits)
'''

# 2차원 리스트

scores = [
[90, 80, 70],   #학생1
[55, 50, 10],   #학생2
[12, 32, 44]    #학생3
]

# 학생 2의 두번째 과목 점수
print(scores[1][1])     # 2차원 리스트의 쓰임 - 이미지, 게임 캐릭터 등
