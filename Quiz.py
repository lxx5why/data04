# 문자메시지 길이에 따라 문자 요금이 결정되는 프로그램
text = input("메시지를 입력하세요: ")
data = len(text)
# 메시지의 길이가 20 이하 50원, 20 초과 100원
if data <= 20:
    print('요금은 50원입니다.')
elif data > 20:
    print('요금은 100원입니다.')
# 사용자로부터 문자메시지를 입력 받아서

# 문자 요금을 출력하는 코드

# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
text = input("점수를 입력하세요: ")
score = int(text)
# 사용자로부터 score를 입력 받아
if 0 <= score <= 20:
    print('E학점입니다.')
elif 21 <= score <= 40:
    print('D학점입니다.')
elif 41 <= score <= 60:
    print('C학점입니다.')
elif 61 <= score <= 80:
    print('B학점입니다.')
elif 81 <= score <= 100:
    print('A학점입니다.')
# 학점으로 환산하여 출력