import random
import time

#
p2 = 0
a2 = 0

###############변수

pl_mable = 10
ai_mable = 10

ai_answer_list = ['홀','짝']
num1_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
num2_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

pl_answer = 0
ai_answer = 0

###############변수

#로딩
def loding():
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)


###############함수

def qna(v, x, y):
    print()
    print (x)
    v = input(y)

    return v

def pl_an(x):

    global pl_answer

    if pl_answer == "홀":
        if ai_M_Num in num1_list:
            x = 'true'
            
        else:
            x = 'false'
           

    elif pl_answer == "짝":
        if ai_M_Num in num2_list:
            x = 'true'
            
        else:
            x = 'false'


    else:
        x = 2

    return x

def ai_an(x):

    global ai_answer

    if ai_answer == "홀":
        if pl_M_Num in num1_list:
            x = 'true'
            
        else:
            x = 'false'
           

    elif ai_answer == "짝":
        if pl_M_Num in num2_list:
            x = 'true'
            
        else:
            x = 'false'

    return x

def sett():
    global pl_mable, ai_mable

    if pl_mable < 0:
        pl_mable = 0

    elif pl_mable > 20:
        pl_mable = 20
        
    if ai_mable < 0:
        ai_mable = 0

    elif ai_mable > 20:
        ai_mable =20

def score():
    print ('==========')
    print ()
    print ('스코어')
    print ()
    print ('ai 구슬: %d개' %ai_mable)
    print ('플레이어 구슬: %d개' %pl_mable)
    print ()
    print ('==========')

def re_answer_hg():
    print()
    print('---------')
    print('홀, 짝으로만 입력해주세요.')
    print('---------')
    print()

def end(a, b):
    print()
    print()
    print()
    time.sleep(1)

    print ('~~~Enter를 눌러 결과확인~~~')

    input()
    print()

    print('걸린 구슬 개수: %d개' %a)
    print('대답: %s' %b)
    print()

def ai_ppt():
    global result, ai_mable, pl_mable, ai_M_Num

    
    if result == 'true':
        print('승리!')
        ai_mable -= ai_M_Num
        pl_mable += ai_M_Num

        sett()
        time.sleep(3)    
        print()
        print()
        score()


    if result == 'false':
        print('패배...')
        ai_mable += ai_M_Num
        pl_mable -= ai_M_Num
        
        sett()
        time.sleep(3)
        print()
        print()
        score()

def pl_ppt():
    global result, ai_mable, pl_mable, ai_M_Num

    
    if result == 'true':
        print('패배...')
        pl_mable -= pl_M_Num
        ai_mable += pl_M_Num

        sett()
        time.sleep(3)    
        print()
        print()
        score()


    if result == 'false':
        print('승리!')
        pl_mable += pl_M_Num
        ai_mable -= pl_M_Num
        
        sett()
        time.sleep(3)
        print()
        print()
        score()


###############함수


#############홀짝게임############

result = 0

while True:

    ####ai턴####

    print('▶ai 턴◀')

    print ('ai가 구슬을 섞는 중입니다.')
    ai_M_Num = random.randint(1,ai_mable)


    loding()


    while True:
        pl_answer = qna(pl_answer, 'ai: 홀? 짝?', '당신: ')
        result = pl_an(result)

        if result == 2:
            re_answer_hg()

        elif result == 'true' or 'false':
            break


    #결과 발표#

    end(ai_M_Num, pl_answer)
    ai_ppt()

    ####ai턴 끝####
    
    if ai_mable < 1 or pl_mable < 1:
        break





    ####pl턴####
    print()
    loding()
    print('▶당신의 턴◀')

    while True:

        print()
        print ('구슬을 몇 개 거시겠습니까?')
        pl_M_Num = int(input('당신: '))
        print()

        if pl_mable < pl_M_Num:
            print('가지고 있는 구슬보다 많은 구슬은 거실 수 없습니다.')

        elif pl_M_Num < 1:
            print('최소 1개 이상의 구슬을 걸어주세요.')

        elif pl_mable > pl_M_Num:
            break

        elif pl_mable == pl_M_Num:
            break

        else:
            print('숫자만 입력 가능합니다.')
        
    print()
    print('당신: 홀? 짝?')

    loding()

    ai_answer = random.choice(ai_answer_list)
    print('ai의 선택: %s ' % ai_answer)

    result = ai_an(result)


    #결과 발표#

    end(pl_M_Num, ai_answer)
    pl_ppt()

    ####pl턴####
    
    if ai_mable < 1 or pl_mable < 1:
        break

    print()
    loding()


loding()
print('=============최종결과=============')

if pl_mable <= 0:
    print('You lose...')
    a2 = 1

elif ai_mable <=0:
    print('You win!')
    p2 = 1


