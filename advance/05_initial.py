class Puppy:

    name = "" # 멤버 변수(필드): class 안에서 사용 가능한 변수
    goal = ""

    def __init__(self,name,goal): # 생성자: 객체화 될 때 호출되는 함수
        # init: 객체화될 때 최초의 이름, 목적을 줌

        # 받아온 name과 goal은 이 생성자를 벗어날 수 없다.(생성자의 쓰임이 다하면 함께 없어진다.)
        # 그래서 클래스(객체) 멤버에다가 넣어줘야, 객체가 살아있는 동안 사용이 가능하다.
        # 그런데 name=name 형태로는 어떤 것이 객체의 멤버인지 알 수 없다.
        # 그래서 멤버인 녀석은 self(이 객체 자신)를 이용하여 표시해준다_객체 안에 저장되어 사라지지 않음

        self.name = name
        self.goal = goal

puppy = Puppy("멍멍이","집지키기") # Puppy를 객체화 하면서 동시에 생성자를 호출하고 -> init에 이름 목적 전달
print(f'이름: {puppy.name} / 목적: {puppy.goal}')

