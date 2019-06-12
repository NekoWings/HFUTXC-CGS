from django.db import models
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse
# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name


class Classroom(models.Model):
    cls_id = models.IntegerField()
    floor = models.IntegerField()
    door1_x = models.IntegerField()
    door1_y = models.IntegerField()
    door2_x = models.IntegerField()
    door2_y = models.IntegerField()
    up_left_x = models.IntegerField()
    up_left_y = models.IntegerField()
    cls_width = models.IntegerField()
    cls_height = models.IntegerField()


@require_http_methods(["GET"])
def add_classroom(request):
    response = {}
    try:
        classroom = Classroom(cls_id=request.Get.get('cls_id'),
                           floor=request.Get.get('floor'),
                           door1_x=request.Get.get('door1_x'),
                           door1_y=request.Get.get('door1_y'),
                           door2_x=request.Get.get('door2_x'),
                           door2_y=request.Get.get('door2_y'),
                           up_left_x=request.Get.get('up_left_x'),
                           up_left_y=request.Get.get('up_left_y'),
                           cls_width=request.Get.get('cls_width'),
                           cls_height=request.Get.get('cls_height'))
        classroom.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
