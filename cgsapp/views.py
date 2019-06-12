from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse, HttpResponse

import os
import json

from .models import Book
# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
 
 
@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def get_blank_map(request):
    response = {}
    try:
        build_id=request.GET.get('build_id')
        # print(type(build))
        if(build=='1'):
            response['msg'] = 'Xinan'
            response['error_num'] = 0
        else:
            response['msg'] = 'Jingting'
            response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def get_start(request):
    response = {}
    try:
        # 从数据库获取起点坐标
        # print(type(build))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
    
@require_http_methods(["GET"])
def get_end(request):
    response = {}
    try:
        # 从数据库获取终点坐标
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def get_route(request):
    response = {}
    try:
        start_pos=request.GET.get(start_pos)
        end_pos=request.GET.get(end_pos)
        # 加载起点终点并返回路径
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
    
@require_http_methods(["GET"])
def get_map(request):
    response = {}
    try:
        build_id=request.GET.get('build_id')
        layers=request.GET.get('layers')
        # 加载起点终点并返回路径
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)

@require_http_methods(["GET"])
def img_test(request):
    d=os.path.dirname(__file__)
    data=request.GET
    file_name=data.get('file_name')

    image_path=os.path.join(d,"static/images/"+file_name+".png")
    image_data=open(image_path,'rb').read()
    return HttpResponse(image_data,content_type="image/png")