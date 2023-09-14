# Generated by Django 4.2.5 on 2023-09-14 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('detail', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
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
            name='MajorTech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major_tech', to='Lectures.major')),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=30)),
                ('point', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('eta', models.URLField(blank=True)),
                ('semester_one', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('semester_two', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')])),
                ('teamplay', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('grade_recommend', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')])),
                ('season_open', models.BooleanField()),
                ('teach', models.BooleanField()),
                ('advance', models.BooleanField()),
                ('category19', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category19_lecture', to='Lectures.category')),
                ('category20', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category20_lecture', to='Lectures.category')),
                ('category21', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category21_lecture', to='Lectures.category')),
                ('category22', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category22_lecture', to='Lectures.category')),
                ('category23', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category23_lecture', to='Lectures.category')),
                ('category24', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category24_lecture', to='Lectures.category')),
                ('former', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='latter', to='Lectures.lecture')),
                ('major', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='major_lecture', to='Lectures.major')),
                ('tech', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='majortech_lecture', to='Lectures.majortech')),
            ],
        ),
    ]
