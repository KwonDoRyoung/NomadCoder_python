# -*-coding: utf-8 -*-
"""
print 함수는 무수히 많은 파라미터를 넣을 수 있음
그러나, 위의 plus 함수는 3개 이상 파라미터를 넣으면 오류가 뜸
position argument = *args
    - 튜플 형태로 전달
keyword argument = **kwargs
    - Dictionary 형태로 전달
"""


# def plus(a, b):
#     return a+b

def plus(a, b, *args, **kwargs):
    return a + b


def plus_inifinite(*args):
    result = 0
    for number in args:
        result += number
    return result


"""
Object Oriented Prog.
객체 지향 언어
class == blueprint
instance == blueprint 로부터 만들어진 결과물
"""


class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4


porche = Car()
print(porche)
print(porche.wheels)
porche.color = "Red"
print(porche.color)

ferrari = Car()
ferrari.color = "Yellow"
print(ferrari.color)

"""
method?
method 첫번째 인자: self = 자기자신
self 자리는 이름은 상관없으나 default: self
class 에는 기본적으로 주어지는 method 가 존재
dir()로 확인 가능
"""


def start():
    print("I am function")


class Car():
    wheels = 4
    doors = 4
    windows = 4
    seats = 4

    def start(self):
        print("I am method")
