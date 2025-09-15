import oper

# dir() 내장 함수를 사용하면 모듈에 정의되어있는 변수, 함수 목록을 볼 수 있음
print(dir(oper))

# 모듈의 이름 확인
print(oper.__name__) # 특정 모듈의 이름을 확인 (별칭인지 본명인지 확인할 때 사용)
print(__name__) # 현재 나의 이름 -> 현재 실행되는 함수

