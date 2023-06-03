import random
import time
if __name__ == "__main__":
    import draw
else:
    from . import draw

#문제를 출제하는 함수
def make_question():
    operand1 = str(random.randint(1, 50))	#1~50사이의 임의의 수
    operand2 = str(random.randint(1, 50))	#1~50사이의 임의의 수
    operator = random.randint(1,4)		#덧셈, 뺄셈, 곱셈, 나눗셈을 랜덤으로

    if (operator == 1):
        q = operand1 + ' + ' + operand2
    if (operator == 2):
        q = operand1 + ' - ' + operand2
    if (operator == 3):
        q = operand1 + ' * '+ operand2
    if (operator == 4):
        q = operand1 + ' / '+ operand2

    return q

def main():
    print("{0:-^50}".format(" 사칙연산 게임 "))
    print(" 정수 또는 실수의 계산 결과를 입력해주세요")
    print(" 결과가 소수일 경우 소숫점 아래 2자리 까지만 입력하세요")
    print(" quit 입력시 나가기")
    print('-' * 56)
    #정답/오답 횟수를 저장한 변수를 초기화
    correct = 0
    wrong = 0
    sum_time = 0
    for x in range(1, 6):			#다섯 문제 출제
        question = make_question()		#문제 출제
        print(question)			#문제 출력
        start = time.time()
        user = 0
        while True:
            try:
                raw = input(" = ")
                if raw == "quit" and draw.ask_quit():
                    return
                user = float(raw)
            except:
                print("다시 입력하세요")
            else:
                break
        end = time.time()
        answer = round(eval(question), 2)

        print("문제", x, "번을 푸는데 걸린 시간 :", round(end-start, 2), "초")
        sum_time = sum_time + end - start
        
        if (user == answer):
            print("정답!")
            correct = correct+1
        else :
            print("오답!", end = ' ')
            print(answer)
            wrong = wrong+1

    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print("모든 문제를 푸는데 걸린 시간 :", round(sum_time,2), "초")
    print("정답 :", correct, "오답 :", wrong)
    draw.ask_continue()

if __name__ == "__main__":
    main()
