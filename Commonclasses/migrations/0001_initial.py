# Generated by Django 4.2.5 on 2023-09-27 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('category21', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category21_common_lecture', to='Majors.category')),
                ('category22', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category22_common_lecture', to='Majors.category')),
                ('category23', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category23_common_lecture', to='Majors.category')),
                ('category24', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category24_common_lecture', to='Majors.category')),
                ('former', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='common_latter', to='Commonclasses.lecture')),
            ],
        ),
        migrations.CreateModel(
            name='UserCommonLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commonlecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commonlecture_completed', to='Commonclasses.lecture')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='commonlecture_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
