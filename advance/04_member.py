class Robot:

    # 생성자: 객체화 할 때 호출되는 함수의 일종으로 객체화가 될 때 가장 먼저 호출된다.
    def __init__(self): # 2. 객체화가 진행 되어서 호출됨
        print('Robot이 복사될 때 제일 먼저 호출되는 멤버') # 3. init이 호출될 때 출력문이 출력됨
        pass

    def doIt(self):
        print('나는 Robot의 함수 입니다.') # 5. doIt 함수 실행될 때 출력문이 출력됨

robot = Robot() # 1. 객체화됨
robot.doIt() # 4. doIt 함수를 실행시킴

