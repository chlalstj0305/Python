# 주석 = 컴퓨터는 알 수 없고, 사람만 알 수 있는 언어
# 이름 = 값 (변수 선언 시, 데이터 타입 필요 없음)
int = 123 # 정수
float = 3.14 # 실수
octal = 0o117 # 8진수(숫자 0과 알파벳 o를 추가)
hex = 0x8ff # 16진수(숫자 0과 알파벳 x를 추가)

# print("int :" +int) # 문자+숫자 형태로는 출력해주지 않는다. (f-string 사용)
# f-string 를 사용하면 문자열과 다른 타입의 데이터를 함께 출력 가능.
print(f'int: {int}')
print(f'flaot: {float}')
print(f'octal: {octal}')
print(f'hex: {hex}') # Tip) 범위지정하고 원하는 기호로 감싸기 가능.


