# Generated by Django 2.2.2 on 2019-06-09 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cgsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cls_id', models.IntegerField()),
                ('is_build_xa', models.BooleanField()),
                ('cls_pos_x', models.IntegerField()),
                ('cls_pos_y', models.IntegerField()),
                ('cls_pos_z', models.IntegerField()),
            ],
        ),
    ]