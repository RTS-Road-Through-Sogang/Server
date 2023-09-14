# Generated by Django 4.2.5 on 2023-09-14 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lectures', '0003_route_subjectinroute_techinsubject_and_more'),
        ('Roadmaps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roadmap',
            name='track',
        ),
        migrations.CreateModel(
            name='SubjectInRoadmapDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roadmap_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Roadmaps.roadmapdetail')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lectures.subject')),
            ],
        ),
    ]
