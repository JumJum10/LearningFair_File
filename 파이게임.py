import random
import time

#변수
pl = 0
ai = 0
ask = 0


########함수########

def info(x):
    print()
    print("게임 설명을 들으시겠습니까?")
    print("네     아니오")
    print()
    answer = input('당신: ')

    if answer == "네":
        x = 1

    elif answer == "아니오":
        x = 0

    else:
        x = 2

    return x

def rechoose():
    print()
    print('---------')
    print('네, 아니오로만 입력해주세요.')
    print('---------')

def loding():
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('.')
    time.sleep(1)

def readyGo():
    loding
    print()
    print('준비가 되면 엔터를 눌러주세요. 게임이 시작됩니다.')
    input()
    print()
    loding()
    print('::게임을 시작합니다.::')
    print()
    time.sleep(1)

def all_result(x, ai, pl):
    print()
    print()
    print('===========%s 결과합산===========' %x)
    print()
    print('ai: 총 %s점' %ai)
    print('플레이어: 총 %s점' %pl)
    print()
    print('================================')
    print()
    print()

def aaaaa(a,b,c,e):
    loding()

    print()
    print()
    print('%s 게임이 끝났습니다.' %a)
    time.sleep(1)
    print('%s의 결과를 발표하도록 하겠습니다.' %b)
    time.sleep(1)
    all_result(b, ai, pl)
    time.sleep(2)
    print('이어서 %s 게임, %s 게임입니다.' %(c,e))
    print()
    print()

########함수########


########게임 설명########

def ranGame_info():
    
    print()
    print('---------')
    print()
    print('※ 게임 방법 ※')
    print()
    print('난수 맞추기 게임은 1~100까지 중 랜덤으로 설정되는 비밀 숫자를 맞추는 게임입니다.')
    print('기회는 총 10번이며, 숫자 입력 시 랜덤값이 그보다 크고 작음을 알려줍니다.')
    print('주어진 기회 안에 랜덤 숫자를 맞추면 플레이어의 승리입니다. \n기회안에 답을 못 맞출 경우 플레이어의 패배입니다.')
    print()
    print('---------')

def mableGame_info():
    
    print()
    print('---------')
    print()
    print('※ 게임 방법 ※')
    print()
    print('홀짝 게임은 상대가 제시한 구슬의 개수가 홀인지 짝인지 맞추는 게임입니다.')
    print('상대가 구슬의 개수를 맞출 경우, 자신이 걸었던 구슬을 모두 상대에게 넘겨줘야 합니다.')
    print('반대로 상대가 구슬의 개수를 맞추지 못 할 경우, 걸려있던 구슬의 개수만큼 상대방이 구슬을 지불해야합니다.')
    print()
    print('---------')

def rpsGame_info():
    
    print()
    print('---------')
    print()
    print('※가위바위보 룰※')
    print()
    print('ai와 가위바위보로 마지막 승부를 겨룹니다.')
    print('가위바위보는 총 3판으로 이뤄지며, 한 번 이길 때마다 1점을 받습니다.')
    print('점수가 같을 시 무승부로 판정이 나고, 무승부가 아닐 시 더 높은 점수를 가진 사람이 최종승리를 하게됩니다.')
    print()
    print('---------')
    print()

########게임 설명########



print('파이게임에 오신 걸 환영합니다.')
time.sleep(1.5)
print('본 프로그램에서는 ai와 세가지 게임을 겨루게 됩니다.')
time.sleep(2)
print('게임의 종류와 순서는 아래와 같습니다.')
time.sleep(1.5)

print()
print()
print('===========게임 리스트===========')
print()
print('Round1. [UpDown게임]')
print('Round2. [홀짝게임]')
print('Round3. [가위바위보]')
print()
print('================================')
print()
print()

time.sleep(1.5)
print('세가지 게임에서 2승을 거둘 시, 플레이어가 승리하게 됩니다.')
time.sleep(1.5)
print('그럼 게임을 시작하겠습니다.')
time.sleep(2)

print()
print()
print()

print('첫번째 게임, UpDown 게임입니다.')






#업다운
while True:
    ask = info(ask)

    if ask == 0:
        break

    elif ask == 1:
        ranGame_info()
        break

    elif ask == 2:
        rechoose()

readyGo()

import updown
from updown import p1
from updown import a1

pl += p1
ai += a1


########Round1 결과 합산########


aaaaa('첫 번째','Round1','두 번째','홀짝 맞추기')


########Round1 결과 합산########






#홀짝
while True:
    ask = info(ask)

    if ask == 0:
        break

    elif ask == 1:
        mableGame_info()
        break

    elif ask == 2:
        rechoose()

readyGo()

import mable
from mable import p2
from mable import a2

pl += p2
ai += a2

########Round2 결과 합산########

aaaaa('두 번째','Round2','마지막','가위바위보')

time.sleep(1)
print('시작 전 간단한 룰 설명이 있겠습니다.')
print(rpsGame_info())

########Round2 결과 합산########






#가위바위보
readyGo()


import last
from last import p3
from last import a3

pl += p3
ai += a3

########Round3 결과 합산########
loding()

print()
print()
print('게임이 모두 끝났습니다.')
time.sleep(1)
print('최종 결과를 발표하도록 하겠습니다.')
time.sleep(1)
all_result('Round3', ai, pl)
time.sleep(2)
loding()


########Round3 결과 합산########


#끝!

print('수고하셨습니다. \n모든 게임이 종료 되었습니다.')
time.sleep(1)

if pl > ai:
    print()
    print('축하드립니다.')
    time.sleep(1)
    print('ai와의 게임에서 승리하셨군요.')
    time.sleep(1)
    print('다음번에도 멋진 승부를 기대하고 있겠습니다.')
    time.sleep(2)
    print()
    print('게임종료')
    time.sleep(1)
    print('프로그램을 종료합니다.')
    time.sleep(1)

elif pl < ai:
    print()
    print('저런...')
    time.sleep(1)
    print('ai와의 게임에서 패배하셨군요. \n오늘은 운이 안 따라준 듯 합니다.')
    time.sleep(1)
    print('다음번에는 행운의 여신이 따라주는 승부를 기대하고 있겠습니다.')
    time.sleep(2)
    print()
    print('게임종료')
    time.sleep(1)
    print('프로그램을 종료합니다.')
    time.sleep(1)

else:
    print()
    print('정말 멋진 경기였습니다.')
    time.sleep(1)
    print('ai와 우열을 가릴 수 없을 정도로요.')
    time.sleep(1)
    print('다음번에도 멋진 승부를 기대하고 있겠습니다.')
    time.sleep(2)
    print()
    print('게임종료')
    time.sleep(1)
    print('프로그램을 종료합니다.')
    time.sleep(1)
