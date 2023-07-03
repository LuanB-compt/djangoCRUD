from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee

import json



def home(request):
    return render(request=request, template_name='index.html')


@csrf_exempt
def create(request):
    if request.method != "POST":
        return HttpResponse(
            JsonResponse(data={'msg':'não recebido'}),
            status=500
        )
    request_json = json.loads(request.body.decode("utf-8"))
    Employee.objects.create(
        name=request_json['name'],
        age=request_json['age'],
        cellphone=request_json['cellphone'],
        position=request_json['position'],
        salary=request_json['salary']    
    )
    return HttpResponse(
        JsonResponse(data={'msg':'recebido'}),
        status=200
    )


@csrf_exempt
def read(request):
    if request.method != "GET":
        return HttpResponse(
            JsonResponse(data={'msg':'error'}),
            status=500
        )
    return HttpResponse(
        JsonResponse(data={'Employees':list(Employee.objects.all().values())}),
        status=200
    )


@csrf_exempt
def update(request, id: int):
    if request.method != "PUT":
        return HttpResponse(
            JsonResponse(data={'msg':'error'}),
            status=500
        )
    request_json = json.loads(request.body.decode("utf-8"))
    fields = [field.name for field in Employee._meta.get_fields()]
    employee = Employee.objects.get(id=id)
    employee.name = request_json['name']
    employee.age = request_json['age']
    employee.cellphone = request_json['cellphone']
    employee.position = request_json['position']
    employee.salary = request_json['salary']
    employee.save()
    return HttpResponse(
        JsonResponse(data={'msg':''}),
        status=200
    )


@csrf_exempt
def delete(request):
    pass