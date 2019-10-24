from django.shortcuts import render
import random
# Create your views here.
def index(request):

    context = {
        'name' : 'nwith',

    }
    return render(request, 'index.html', context)

def dinner(request):
    foods = ['초밥', '카레', '칼국수']
    pick = random.choice(foods)
    context = {
        'pick':pick,
    }
    # Template Variable
    return render(request, 'dinner.html', context)

# Variable Routing
def hello(request, name): #url pattern이랑 항상 name은 같아야함.
    context = {
        'name':name,
    }

    return render(request, 'hello.html', context)


#[실습]
# 1. 이름과 나이를 variable routing을 통해 받아서 자기소개
def hi(request, name, age):
    context = {
        'name':name,
        'age':age,
    }
    return render(request, 'hi.html',context)

#[실습]
# 숫자 2개를 받아 두개의 곱셈을 출력하는.
def times(request, num1, num2):
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : num1*num2
    }
    return render(request, 'times.html',context)