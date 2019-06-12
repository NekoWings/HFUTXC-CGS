from django.db import models

# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name


class Classroom(models.Model):
    cls_id = models.IntegerField()
    is_build_xa = models.BooleanField()
    cls_pos_z = models.IntegerField()
    door1_x = models.IntegerField()
    door2_x = models.IntegerField()
    door1_y = models.IntegerField()
    door2_y = models.IntegerField()
