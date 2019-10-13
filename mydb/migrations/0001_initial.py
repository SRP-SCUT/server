# Generated by Django 2.2 on 2019-09-11 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomId', models.CharField(max_length=80)),
                ('maxCap', models.IntegerField(default=0)),
                ('roomType', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'rooms',
            },
        ),
        migrations.CreateModel(
            name='rooms_teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomId', models.CharField(max_length=80)),
                ('teacherId', models.CharField(max_length=80)),
                ('date', models.CharField(max_length=80)),
                ('time', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'rooms_teacher',
            },
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacherId', models.CharField(max_length=80)),
                ('weChatId', models.CharField(max_length=80)),
                ('name', models.CharField(default='NoUserNick', max_length=255)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
    ]
