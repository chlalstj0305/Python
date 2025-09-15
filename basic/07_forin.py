# for문은 반복 횟수가 정해진 상태에 적합함.
# 구조: for [하나씩 가져올 변수] in range[범위]:

# 예시) 물 10잔 떠 오기
for cup in range(1,11):
    print(f'물 {cup}잔 떠왔습니다.')

# 2중 FOR문: 반복 안에 반복 발생
# 만약 커피를 타는데 한잔의 물에 믹스 2개씩을 넣어야 한다면?
for cup in range(1,11):
    print(f'물 {cup}잔 떠왔습니다.')
    for coffee_mix in range(1,3):
        print(f'{coffee_mix}개의 믹스를 넣었습니다.')
        for spoon in range(1,4):
            print(f'{spoon}번 수픈으로 젖는다.')

