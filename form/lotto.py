# 명령어 pip list | grep requests   -> requests 설치되어있는지 확인하기 

import requests

n = input('회차를 입력하세요: ')

url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'

# get과 post방식이 있는데, 궁금하면 찾아보기로.
response = requests.get(url) 
lotto = response.json() # .text는 str / .json는 dict


winner = []
#for i in range(1, 7):
#    winner.append(lotto[f'drwtNo{i}'])

winner.append([lotto[f'drwtNo{i}'] for i in range(1,7)])  # 이처럼 짜면 속도측면에서도 빠르다.


bonus = lotto['bnusNo']

print(f'당첨 번호는 {winner} + {bonus}입니다.')