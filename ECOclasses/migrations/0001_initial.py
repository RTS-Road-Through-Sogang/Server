# Generated by Django 4.2.7 on 2023-11-07 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=30)),
                ('point', models.IntegerField(choices=[(1, '1point'), (2, '2point'), (3, '3point')])),
                ('eta', models.URLField(blank=True)),
                ('semester_one', models.IntegerField(blank=True, choices=[(0, 'none'), (1, 'sometimes'), (2, 'little'), (3, 'many')])),
                ('semester_two', models.IntegerField(blank=True, choices=[(0, 'none'), (1, 'sometimes'), (2, 'little'), (3, 'many')])),
                ('teamplay', models.IntegerField(blank=True, choices=[(0, 'none'), (1, 'little'), (2, 'average'), (3, 'much'), (4, 'full')])),
                ('former', models.CharField(blank=True, max_length=30, null=True)),
                ('grade_recommend', models.CharField(max_length=10)),
                ('season_open', models.BooleanField()),
                ('label', models.CharField(max_length=30)),
                ('teach', models.BooleanField()),
                ('advance', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='MajorTech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='MajorTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complete_point', models.IntegerField()),
                ('gicho_point', models.IntegerField()),
                ('duty_point', models.IntegerField()),
                ('choice_point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='UserECOLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecolecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ecolecture_completed', to='ECOclasses.lecture')),
            ],
        ),
    ]
