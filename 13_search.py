# 검색 -> 특정한 자료 덩어리에서 원하는 값을 찾는 것 (index 사용)
a = [3,4,1,2,3,4,'G','F','G']

# 원하는 값의 인덱스 찾기
# 2 라는 값은 어느 위치에 있는가?
print(f'2는 어디?: {a.index(2)}')

# G 라는 값은 어느 위치에 있는가?
print(f'G는 어디?: {a.index('G')}') # 문제점: G는 2개인데 처음 찾은 값만 알려줌
# 5번 인덱스부터 G를 찾아라
print(f'G는 어디?: {a.index('G',5)}')

# 값이 없으면 에러(예외)를 발생시킨다.
# print(a.index('H')) # ValueError: 'H' is not in list

# 모든 3을 찾아보세요. (방법1)
b = [3,4,1,2,3,4,5,6,1,3,2]
print(f'3은 어디?: {b.index(3,0)}')
print(f'3은 어디?: {b.index(3,1)}')
print(f'3은 어디?: {b.index(3,5)}')


# 모든 3을 찾아보세요. (방법2)
# 코드: b라는 리스트에서 3이 어디 인덱스에 위치해 있는지 모두 찾기 위함.
# b = [3,4,1,2,3,4,5,6,1,3,2]             # 리스트를 생성해서 변수b에 담기
# idx = 0                                 # 0을 변수 idx에 담기 (idx 기능: 찾는 값(3)의 위치 표시& index 함수의 시작점)
# while True:                             # while 반복문과 index 함수 사용해서 3의 위치 찾기 (조건을 참으로 설정 -> 무한반복)
#     idx = b.index(3,idx)                # idx의 위치에서부터 시작해서 3을 찾을 거임 -> idx = 0이기 때문에 0번째 인덱스부터 시작 -> 찾은 인덱스를 idx에 담음
#     print(f'3의 값은 {idx}번에 있다.')     # 3의 값은 idx번에 있다. 출력
#     idx += 1                            # idx에 +1을 하고 반복해서 3의 인덱스를 찾음 왜? 안 하면 같은 위치에서 계속 찾으니까 -> 더이상 위치를 찾을 3이 없으면 에러 -> 종료


# 모든 3을 찾아보세요. (방법3)
b = [3,4,1,2,3,4,5,6,1,3,2]
idx = 0
for n in b: # for in을 이용하면 list에 있는 값을 순서대로 하나씩 뽑아낸다.
    if n == 3:
        print(f'3이 있는 인덱스 : {idx}')
    idx += 1

# 리스트 요소 삭제
# del a[3] 과 a.remove(3)
# del은 특정 인덱스의 값을 지움
# remove는 해당 값을 지움 (한 개만)
print(f'a : {a}')
a.remove(3)
print(f'a : {a}')

# pop() = append() 의 반대 개념
# 맨 마지막 요소를 빼낸다.(= 리스트에서 사라진다.)
val = a.pop()
print(f'빼낸 값 : {val} / a: {a}')
val = a.pop()
print(f'빼낸 값 : {val} / a: {a}')

# 리스트 확장(더하기와 비슷한 개념)
print(a)
a.extend(b)
print(a)

# count(value) - 특정한 값이 해당 리스트에 몇 개 있는지 확인
print(a)
print(f'a 안에 3은 {a.count(3)}개가 있다.')
print(f'a 안에 9는 {a.count(9)}개가 있다.') # 없는 값은 0을 반환

print('-'*20)

# a 안에 있는 모든 3을 지워주세요. 방법(1)
for n in a:
    if n == 3:
        a.remove(3)
print(a)
# a 안에 있는 모든 3을 지워주세요. 방법(2)
while True:
    a.remove(3)
    if a.count(3) == 0:
        break
print(a)