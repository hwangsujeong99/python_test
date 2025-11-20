weater = "비"

if weater == "비":  #들여쓰기로 중괄호 구분
    print("우산을 챙기세요")

    ###    = VS ==
    # x = 5     //할당 -? z에 5를 저장
    # X == 5 // 비교 -> x가 5와 같은가?

    ## 비교 연산자들

    age = 20

    # 같다

    if age == 20:
        print("같음")
    # 다르다
    if age != 25:
        print("나이가 25살이 아닙니다.")
    # 크다
    if age > 18:
        print("성인")

    #작다
    if age < 30:
        print("30살  미만")

    #크거나 같다(이상) / age >=
    if weater == "비":
        print("우산을 챙기세요")
    else:
        print("좋은 날씨네요~!")

    # if - elif - else : 여러 조건
    score = 85

    if score >= 90:
        print("A등급")
    elif score >=80:  # 시스템 자원을 효율적으로 사용 가능
        print("B등급")
    elif score >=70:
        print("C등급")
    else :
        print("F등급")

    # 논리 연산자 :
    # and : 둘 다 참이어야 함
    age = 25
    height = 180

    if age >= 18 and height >= 170:
        print("놀이기구 탑승 가능합니다.")

    # or : 하나라도 참이면 참
    day = "토요일"
    if day == "토요일" or day == "일요일":
        print("주말입니다 ~ !! ")

    # not
    is_raining = False
    if not is_raining: # 거짓 -> 참으로 변경
        print("비가 안 오네요")

    #영화관 입장료 계산기
    #age = int(input("나이를 입력하세요: ")) #입력 받기
    #print(age)

    '''
    규칙:
        13세 미만 : 5000원
        13세 이상 ~ 18세 미만 : 8000원
        18세 이상 ~ 65세 미만 : 12000원
        65세 이상: 7000원
    '''

    age = int(input("나이를 입력하세요: "))
    if age < 13:
        price = 5000
    elif age >= 13 and age < 18:
        price = 8000
    elif age >= 18 and age < 65:
        price = 12000
    else:
        price = 7000

    print(f"입장료: {price}원 입니다.")


