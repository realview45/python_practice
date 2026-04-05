# 숫자자료형
print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))
# 문자열자료형
print('풍선')
print("나비")
print("ㅋ"*9)
# boolean자료형
print(5 > 10)
print(True)
print(not True)
# 변수 
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >=3
print("우리집 " + animal + "의 이름은 " + name + "에요.")
print(name + "는 " + str(age) + "살이에요")
#,를 이용하면 정수형, boolean도 str로 감싸지않고, 실행가능 그러나 띄어쓰기 무조건포함
print(name + "는 " ,age, "살이에요")
print(name + "은 어른일까요?" + str(is_adult))
'''
여러문장 주석처리
ctrl + / : 주석처리 단축키
퀴즈
'''
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")