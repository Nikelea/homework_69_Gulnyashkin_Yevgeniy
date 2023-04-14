import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import numbers
from decimal import Decimal


def json_echo_view(request, *args, **kwargs):
    respon = {}
    if request.method == 'POST':
        if request.body:
            if isinstance(json.loads(request.body)['a'], numbers.Number) and isinstance(json.loads(request.body)['b'], numbers.Number):
                answer = json.loads(request.body)['a'] + json.loads(request.body)['b']
                respon['answer'] = answer
            else:
                respon['error'] = 'Введите числа'
    return JsonResponse(respon)


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')
  

def check_input(input):
    if json.loads(input.body)['a'].replace('.', '', 1).isdigit() and json.loads(input.body)['b'].replace('.', '', 1).isdigit():
        return True
    else:
        return False


def add_view(request, *args, **kwargs):
    respon = {}
    if request.method == 'POST':
        if request.body:
            if check_input(request):
                answer = Decimal(json.loads(request.body)['a']) + Decimal(json.loads(request.body)['b'])
                respon['answer'] = answer
            else:
                response = JsonResponse({'error': 'Введите числа'})
                response.status_code = 400
                return response
    return JsonResponse(respon)  


def subsrtact_view(request, *args, **kwargs):
    respon = {}
    if request.method == 'POST':
        if request.body:
            if check_input(request):
                answer = Decimal(json.loads(request.body)['a']) - Decimal(json.loads(request.body)['b'])
                respon['answer'] = answer
            else:
                response = JsonResponse({'error': 'Введите числа'})
                response.status_code = 400
                return response
    return JsonResponse(respon)  


def divide_view(request, *args, **kwargs):
    respon = {}
    if request.method == 'POST':
        if request.body:
            if check_input(request):
                if Decimal(json.loads(request.body)['a']) != 0 and Decimal(json.loads(request.body)['b']) != 0:
                    answer = Decimal(json.loads(request.body)['a']) / Decimal(json.loads(request.body)['b'])
                    respon['answer'] = answer
                else:
                    response = JsonResponse({'error': 'Делить на ноль нельзя!'})
                    response.status_code = 400
                    return response
            else:
                response = JsonResponse({'error': 'Введите числа'})
                response.status_code = 400
                return response
    return JsonResponse(respon)  


def multiply_view(request, *args, **kwargs):
    respon = {}
    if request.method == 'POST':
        if request.body:
            if check_input(request):
                answer = Decimal(json.loads(request.body)['a']) * Decimal(json.loads(request.body)['b'])
                respon['answer'] = answer
            else:
                response = JsonResponse({'error': 'Введите числа'})
                response.status_code = 400
                return response
    return JsonResponse(respon)  
     