# 9월 12일 수업 내용

# 사전은 {키:값} 형태로 되어있다.
# 비슷한 자료구조로, 자바스크립트에는 오브젝트/ 자바에는 맵이 있다.
dic = {'name':'chlalstj',
       'phone':'010-1234-1234',
       'age':24
}

dic2 = {
    'name':'hong,gil-dong',
    'phone':'010-2233-5454',
    'friends': ['Alice','John','Smith']
}

# 사전에 데이터 넣기1
a = {'first':'a'}
print(a)

# 사전에 데이터 넣기2
a['second'] = 'b'
print(a)

# 사전에서 특정 요소 삭제
del a['second']
print(a)

# 사전의 특정 요소를 꺼내보자. 방법1 (사용법은 List와 비슷하다.)
print(dic2['name'])
print(dic2['friends'])

# 사전의 특정 요소를 꺼내보자. 방법2_get 함수 사용
print(dic2.get('phone'))
print(dic2.get('nick','해당 내용이 없음')) # 특정 키가 없는 경우 None이 아닌 대체 내용으로 반환 할 수 있음