# 산술연산
print(1+1)# 2
print(3-2)# 1
print(5*2)# 10
print(6/3)#나누기 2.0?
print(5%3)#나머지 2
print(10%3)#1
print(5//3)#몫 1

# 비교연산
print(10 > 3) #True
print(4 >= 7) #False
print(10 < 3) #False
print(3 >= 3) #True

print(3 == 3) #True
print(4 == 2) #False
print(3 + 4 == 7) #True

print(1 != 3) #True
print(not(1!=3)) #False

print((3>0) and (3<5)) #True
print((3>0) & (3<5)) #True

print((3>0) or (3>5)) #True
print((3>0) | (3>5)) #True

#5는 4보다크고 4는 3보다크다
print(5 > 4 > 3) #True
print(5 > 4 > 7) #False

print(abs(-5))#5
print(pow(4,2))#4^2 = 4*4 = 16
print(max(5,12))#12
print(min(5,12))#5

from math import *
print(floor(4.99))#내림 4
print(ceil(3.14))#올림 4
print(sqrt(16))#제곱근 4.0

from random import *
print(random()) #0.0 ~ 1.0미만의 임의의 값 생성
print(random()*10) #0.0 ~ 10.0미만의 임의의 값 생성
print(int(random()*10)) #0 ~ 10미만의 임의의 정수 값 생성
print(int(random()*10)+1) #1 ~ 11미만의 임의의 정수 값 생성
print(int(random()*45)+1)
print(randrange(1,46)) #1 ~ 46미만의 임의의 값 생성
print(randint(1,45)) #1 ~ 45이하

#랜덤으로 날짜뽑기
#월별 날짜는 다름을 감안하여 28일이내
#매월 1~3일은 스터디 준비를 해야하므로 제외
from random import *
# day = int(random()*28)+1
day = randint(4,28)
print(str(day)+"일입니다.")

#문자열
sentence='나는 소년입니다.'
print(sentence)
sentence2="파이썬은 쉬워요"
print(sentence2)
sentence3="""
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)