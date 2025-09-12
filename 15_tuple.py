tu1 = (1,2,3) #tuple은 []가 아닌 ()로 선언
tu2 = ('a','b','c')
tu3 = (1,2,('a','b'))

# 불러오기
print(tu1[1])
# slicing
print(tu2[1:])
# 더하기
print(tu1+tu2)
# 곱하기
print(tu1*3)

# tuple <-- --> list 간의 전환
tu2list = list(tu2) # list 함수 사용
print(f'{tu2} -> {tu2list}') # 전환 확인

# list <-- --> tuple 간의 전환
list2tu = tuple(tu2list) # tuple 함수 사용
print(f'{tu2list} -> {list2tu}') # 전환 확인
