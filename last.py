import random
import time

#
p3 = 0
a3 = 0


#변수/리스트
ai_rps_list = ['가위','바위','보']
pl_rps = 0

ai_score = 0
pl_score = 0


#로딩
def loding():
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)


def rechoose():
    print()
    print('---------')
    print('가위, 바위, 보 중에 하나로 입력해주세요.')
    print('---------')
    print()

def rps_ppt(a, b):
    print()
    print('ai: %s' %a)
    print('당신: %s' %b)
    print()
    print('~~~Enter를 눌러 다음으로 넘기기~~~')
    input()

def rps_loding():
    print()
    time.sleep(1)
    print('안 내면 진다!')
    time.sleep(1)
    print('가위!')
    time.sleep(1)
    print('바위!')
    time.sleep(1)
    print('보!')
    time.sleep(1)

def who_win(ai_answer, pl_answer):
    if ai_answer == '가위':
        if pl_answer == '가위':
            result = 0
            print()
            print ('무승부')
        
        elif pl_answer == '바위':
            result = 1
            print()
            print ('승리!')
        

        elif pl_answer == '보':
            result = 2
            print()
            print ('패배...')
        

    elif ai_answer == '바위':
        if pl_answer == '가위':
            result = 2
            print()
            print ('패배...')
        
        elif pl_answer == '바위':
            result = 0
            print()
            print ('무승부')

        elif pl_answer == '보':
            result = 1
            print()
            print ('승리!')


    elif ai_answer == '보':
        if pl_answer == '가위':
            result = 1
            print()
            print ('승리!')
        
        elif pl_answer == '바위':
            result = 2
            print()
            print ('패배...')

        elif pl_answer == '보':
            result = 0
            print()
            print ('무승부')
    
    return result

def end(result, pl_score, ai_score):
    if result == 0:
        pass

    elif result == 1:
        pl_score += 1

    elif result == 2:
        ai_score += 1

    return pl_score, ai_score

def rps_ppt2(pl_score, ai_score):
    print()
    print('====현재 스코어====')
    print('ai: %s' %ai_score)
    print('당신: %s' %pl_score)
    print()
    print()
    print()



#############가위바위보############


for i in range(3):

    print('~~~~~~~%s ROUND!~~~~~~~' % (i+1))

    ai_answer = random.choice(ai_rps_list)
    print()
    print('어떤 걸 내시겠습니까? [가위, 바위, 보]: ')

    while True:
        pl_rps = input('당신: ')

        if pl_rps == '가위':
            break

        elif pl_rps == '바위':
            break

        elif pl_rps == '보':
            break

        else:
            rechoose()

    rps_loding()

    print()
    print()
    rps_ppt(ai_answer, pl_rps)
    print()
    print()

    result = who_win(ai_answer, pl_rps)
    pl_score, ai_score = end(result, pl_score, ai_score)

    rps_ppt2(pl_score, ai_score)
    time.sleep(1)

if pl_score == ai_score:
    print ('결과: 무승부')

elif pl_score > ai_score:
    print ('결과: You win!')
    p3 = 1

elif pl_score < ai_score:
    print ('결과: You lose...')
    a3 = 1


