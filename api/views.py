from django.shortcuts import render
from .models import *
from .serializers import StudentUserserializer
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def data1(request):
    if request.method == 'GET':
        stu = StudentUser.objects.all()
        serializer = StudentUserserializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)


def data(request,pk):
    if request.method == 'GET':
        stu = StudentUser.objects.get(id=pk)
        serializer = StudentUserserializer(stu)
        return JsonResponse(serializer.data)


@csrf_exempt
def create_data(request):
    if request.method == "POST" :
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer= StudentUserserializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg': 'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def update_data(request):
    if request.method == 'PUT':
        json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id=python_data.get('id')
    stu = StudentUser.objects.get(id=id)
    serializer = StudentUserserializer(stu,data=python_data,partial=True)
    if serializer.is_valid():
        serializer.save()
        res = {'msg': 'Data Updated'}
        json_data = JSONRenderer().render(res)
        return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def delete(request):
    if request.method == 'DELETE':
        json_data = request.body
    stream = io.BytesIO(json_data)
    python_data = JSONParser().parse(stream)
    id=python_data.get('id')
    stu = StudentUser.objects.get(id=id)
    stu.delete()
    res = {'msg': 'data deleted'}
    # json_data = JSONRenderer().render(res)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(res,safe=False)


