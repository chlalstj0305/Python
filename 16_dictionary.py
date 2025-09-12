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
