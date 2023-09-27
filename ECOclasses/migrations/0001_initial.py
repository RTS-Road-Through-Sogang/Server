# Generated by Django 4.2.5 on 2023-09-27 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Majors', '0001_initial'),
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
                ('semester_one', models.IntegerField(blank=True, choices=[(1, 'low'), (2, 'mid'), (3, 'high')])),
                ('semester_two', models.IntegerField(blank=True, choices=[(1, 'low'), (2, 'mid'), (3, 'high')])),
                ('teamplay', models.IntegerField(blank=True, choices=[(1, 'none'), (2, 'little'), (3, 'average'), (4, 'much'), (5, 'full')])),
                ('grade_recommend', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('season_open', models.BooleanField()),
                ('teach', models.BooleanField()),
                ('advance', models.BooleanField()),
                ('category21', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category21_ECO_lecture', to='Majors.category')),
                ('category22', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category22_ECO_lecture', to='Majors.category')),
                ('category23', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category23_ECO_lecture', to='Majors.category')),
                ('category24', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category24_ECO_lecture', to='Majors.category')),
                ('former', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ECO_latter', to='ECOclasses.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='UserECOLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ecolecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ecolecture_completed', to='ECOclasses.lecture')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ecolecture_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ECO_track', to='Majors.major')),
                ('student_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ECO_studentyear_track', to='Users.studentyear')),
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
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major_ECOtrack', to='Majors.major')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_ECOtrack', to='ECOclasses.track')),
            ],
        ),
        migrations.CreateModel(
            name='MajorTech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ECO_tech', to='Majors.major')),
            ],
        ),
        migrations.AddField(
            model_name='lecture',
            name='tech',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='majortech_ECO_lecture', to='ECOclasses.majortech'),
        ),
    ]
