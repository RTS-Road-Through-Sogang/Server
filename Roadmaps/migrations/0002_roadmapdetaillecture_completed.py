# Generated by Django 4.2.5 on 2023-10-03 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Roadmaps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roadmapdetaillecture',
            name='completed',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
