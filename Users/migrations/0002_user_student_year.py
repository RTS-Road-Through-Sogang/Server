# Generated by Django 4.2.5 on 2023-09-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_year',
            field=models.IntegerField(default=0, null=True),
        ),
    ]