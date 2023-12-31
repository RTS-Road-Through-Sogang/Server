# Generated by Django 4.2.5 on 2023-11-08 05:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CSEclasses', '0001_initial'),
        ('Commonclasses', '0001_initial'),
        ('MGTclasses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ECOclasses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roadmap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_roadmap', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoadmapDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.CharField(max_length=20)),
                ('roadmap', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roadmap_detail', to='Roadmaps.roadmap')),
            ],
        ),
        migrations.CreateModel(
            name='RoadmapDetailLecture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False, null=True)),
                ('commonlecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cselecture_roadmap_detail', to='Commonclasses.lecture')),
                ('cselecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cselecture_roadmap_detail', to='CSEclasses.lecture')),
                ('ecolecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ecolecture_roadmap_detail', to='ECOclasses.lecture')),
                ('mgtlecture', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mgtlecture_roadmap_detail', to='MGTclasses.lecture')),
                ('roadmap_detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roadmap_detail', to='Roadmaps.roadmapdetail')),
            ],
        ),
    ]
