dic = {
    'name':'hong,gil-dong',
    'phone':'010-1234-1234',
    'friends':['Alice','Smith','John']
}

# dic.keys() : 특정한 사전의 키들만 가져와 dict_keys 라는 객체를 반환
print(dic.keys())
for item in dic.keys(): # 사전의 key만 가져오고 싶은 경우
    print(item)

# dict_keys -> list 로 변환
keys = list(dic.keys()) # key를 list로 변환
print(keys)

# dict.values() : 특정 사전의 값만 가져와 dict_values 라는 객체를 반환
print(dic.values())

# list로 변경해서 values 라는 변수에 담아보자
values = list(dic.values())
print(values)

# dic.items() : 사전의 {키:값}을 한 쌍으로 가져와 dict_items로 반환
# 각 키와 값은 () 모양으로 보아 tuple 이다.
print(dic.items())
li = list(dic.items()) # list로 변환
print(li)

# 값을 가져오기
print(dic.get('name'))
print(dic['phone'])

print('-'*30)

# dic 안에 있는 모든 키와 값을 키:값 형태로 출력해보자.
# 1. 키를 뽑아낸다음, 키를 가지고 값을 뽑아내는 방법
for item in dic.keys():
    print(f'{item}:{dic.get(item)}')
# 2. 키와 값을 동시에 뽑아낸 다음 거기서 키와 값을 각각 추출하는 방식
for  item in dic.items():
    print(f'{item[0]}:{item[1]}')


# 90이상인 사람의 이름만 출력
members = {
    'kim':63, 'lee':88, 'park':97, "gang":77, "hwang":100, "ga":65,
    "na":92, "la":90, "wang":100, "gu":79
}

for item in members.items():
    if item[1] >= 90:
        print(f'이름 : {item[0]}')


# key in dic : 해당 키가 사전에 존재하는지 확인
# 검색 시작 여부를 결정할 수 있는 방법
yn = 'kim' in members # 있으면 True
print(f'kim이 있는가? {yn}')

yn = 'jung' in members # 없으면 False
print(f'jung이 있는가? {yn}')

# update : 이미 있는 키면 수정을, 없는 키면 추가를 하는 함수
dic.update({'name':'홍길동','age':30,'married':False})
print(dic)

# dic.clear() : 사전 안의 내용을 모두 지운다.
dic.clear()
print(dic)
