import random
import time

#
p1 = 0
a1 = 0

def loding():
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)

#####게임시작#####


ranNum = random.randint(1,101)
count = 10
userNum = int (input ('숫자를 입력하세요: '))

for i in range (10, 0, -1):

    if userNum < ranNum:
        count -= 1
        print()
        print ('그 값보다는 큰 수 입니다. (남은 기회: %d)' %count)
        userNum = int (input('당신: '))
        
    elif userNum > ranNum :
        count -= 1
        print()
        print ('그 값보다는 작은 수 입니다. (남은 기회: %d)' %count)
        userNum = int (input('당신: '))
        
    elif userNum == ranNum:
        break

    

if count > 0:
    p1 = 1
    print()
    print ('정답입니다.')
    print()
    loding()
    print('You win!')

else:
    a1 = 1
    print()
    print ('게임오버')
    print ('정답:',ranNum)
    print()
    loding()
    print('You lose...')


