import random

number = random.randint(1,31)
print(f'내 마음 속 숫자: {number}')
running = True


while running:
    # 입력 받은 값을 정수(int)로 변환하여 guess에 대입
    guess = int(input('1~31 중 내가 생각한 숫자는?'))
    if guess == number:
        running = False
        print('정답입니다.')
    elif guess < number:
        print(f'당신이 생각한 {guess}보다 정답은 큽니다.')
    elif guess > number:
        print(f'당신이 생각한 {guess}보다 정답은 작습니다.')
    else:
        print('다른 수를 입력하세요.')
    print(f'입력 받은 숫자: {guess}')

