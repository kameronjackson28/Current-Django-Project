# Generated by Django 3.1.6 on 2021-02-16 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('course_number', models.IntegerField(max_length=10)),
                ('instructor_name', models.CharField(default='', max_length=100)),
                ('duration', models.FloatField()),
            ],
        ),
    ]
