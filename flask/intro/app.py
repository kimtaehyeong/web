
# ctrl + `
# control + shift + p 
# 만약 파일 명이 app.py 면, FLASK_APP=hello.py 식으로 안해두 그냥 실행 된다. [flask run] - 실행

# __name__이 직접 실행되면, .py 이름값이 __main__ 
# import 로 실행되면, __name__ 은 - app.py 들어오고
from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/') # @ 데코레이터 함수를 인자로 받는
# 누군가 어떤 주소로 접근을 했을떄 뒤에 / 를 더 붙여서..
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

# http://127.0.0.1:5000/mulcam 으로 접속하면, ~_~ 아래 함수가 실행된다.
@app.route('/mulcam')
def mulcam():
    return 'This is mulcam!'


# # 위에 두가지 방법으로 실행을 시켰었는데
# # 원래는 app.run(Debug=True) 으로 실행해야된다. 하지만 위에처럼 실행하면 자동으로 실행된다.
# # python app.py
# if __name__ == '__main__':
#     app.run(debug=True)


# Path Variable / Variable Routing
# http://127.0.0.1:5000/greeting/hi - 이런식으로 사용가능
@app.route('/greeting/<string:name>')
def greeting(name):
    return f'HI, {name}' # 'Hi, {}'.format(name)


@app.route('/cube/<int:num>')
def cube(num):
    result =  num ** 3
    return f'{num}의 세제곱은 {result}입니다.'


# 사람 수를 Path를 통해 받아, 사람 수 만큼 메뉴 추천
import random
@app.route('/kth/<int:person>')
def kth(person):
    

    food = ['햄버거','피자','스파게티','삼겹살','소고기']
    
    result = random.sample(food, person)
    # result는 리스트로 받게 되니, ','.join(result) 로 써도 가능.
    return f'{result}'

@app.route('/html/')
def html():
    multiline = """
        <h1>Hi, Hello</h1>
        <p>만나서 반갑습니다!</p>
    """
    return multiline

@app.route('/html_file')
def html_file():

    return render_template('file.html')


#Template Variable
@app.route('/hi/<string:name>')
def hi(name):
    return render_template('hi.html', your_name=name)

@app.route('/list')
def list1():
    food = ['햄버거','피자','스파게티','삼겹살','소고기']
    return render_template('list.html', food=food)