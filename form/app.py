from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/fake_naver')
def fake_naver():
    return render_template('fake_naver.html')

@app.route('/fake_google')
def fake_google():
    return render_template('fake_google.html')

# 데이터 보내는쪽
@app.route('/send')
def send():
    return render_template('send.html')


# 데이터 받는 쪽
@app.route('/receive')
def receive():
    username = request.args.get('username') # print -> {'username':'mwith', 'messgae':'안녕'}
    message = request.args.get('message')

    # ....

    return render_template('receive.html', username=username, message=message)


# 회차를 볼 수 있는 페이지
@app.route('/check_lotto')
def check_lotto():
    return render_template('check_lotto.html')

# 결과를 볼 수 있는 페이지
@ app.route('/result_lotto')
def result_lotto():
    n = request.args.get('round_lotto') # request.args['round_lotto'] -> n = input('회차를 입력하세요: ')
    numbers = list(map(int, request.args.get('numbers').split())) # [1,2,3,4,5,6]
    # [int(number) for number in request.args.get('numbers').split()]
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'

    # get과 post방식이 있는데, 궁금하면 찾아보기로.
    response = requests.get(url) 
    lotto = response.json() # .text는 str / .json는 dict


    winner = []
    #for i in range(1, 7):
    #    winner.append(lotto[f'drwtNo{i}'])

    winner = [lotto[f'drwtNo{i}'] for i in range(1,7)]  # 이처럼 짜면 속도측면에서도 빠르다.
    bonus = lotto['bnusNo']
    
    
    matched = list(set(numbers) & set(winner)) # 중복되는 숫자들
    count = len(matched)

    if count == 6:
        result = '1등입니다!!!'
    elif count == 5:
        if bonus in numbers:
            result = '2등입니다!!'
        else:
            result = '3등입니다!!!'
    elif count == 4:
        result = '4등입니다!!!'
    elif count == 3:
        result = '5등입니다!!!'
    else:
        result = '꽝입니다 ㅠㅠ'

    return render_template('result_lotto.html', winner=winner, bonus=bonus, n=n, result=result, numbers=numbers) # 전달할 수 있도록 변수를 넘겨준다.

if __name__ == '__main__':
    app.run(debug=True)

