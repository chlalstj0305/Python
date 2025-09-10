# 문자열은 ''(싱글쿼터) 또는 ""(더블쿼터) 모두 사용 가능
# Tip) 자동 완성 끄고 싶은 경우: ESC
name = 'choi min seo'
content = "My content"
age = 33

# 여러줄의 문자열을 변수에 담을 때 (''''''사용)
multi = '''this is multi line string
this is second line'''

print('name: '+name)
print('content: '+content)
print('multi: '+multi) # 문자열끼리는 f-string 사용할 필요x

# 문자열에 다른 타입의 데이터를 함께 출력할 경우
# 방법1. format 사용
# 방법2. 숫자를 문자로 변환: str 함수 사용
# 방법3. f-string 사용
print('내 이름은 {0} 이고, 나이는 {1} 입니다.'.format(name,age))
print('내 이름은 '+name+' 이고, 나이는 '+str(age)+' 입니다.')
print(f'내 이름은 {name} 이고, 나이는 {age} 입니다.')

# 여러줄 -> 한줄 처리/ 한줄 -> 여러 줄처럼 줄 바꿈 하는 방법
print('이것은 한 줄 이지만\n 여러 줄처럼 보이게 할 겁니다.')
print('이것은 두 줄 이지만 \
한 줄처럼 보이게 할 겁니다.')
