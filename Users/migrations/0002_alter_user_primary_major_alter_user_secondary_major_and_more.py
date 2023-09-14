# Generated by Django 4.2.5 on 2023-09-14 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='primary_major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_major_users', to='Users.major'),
        ),
        migrations.AlterField(
            model_name='user',
            name='secondary_major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_major_users', to='Users.major'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.studentnumber'),
        ),
    ]
