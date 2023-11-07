# Generated by Django 4.2.7 on 2023-11-07 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Users', '0001_initial'),
        ('CSEclasses', '0001_initial'),
        ('Majors', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usercselecture',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cselecture_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='track',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CSE_track', to='Majors.major'),
        ),
        migrations.AddField(
            model_name='track',
            name='student_year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CSE_studentyear_track', to='Users.studentyear'),
        ),
        migrations.AddField(
            model_name='majortrack',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='major_CSEtrack', to='Majors.major'),
        ),
        migrations.AddField(
            model_name='majortrack',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track_CSEtrack', to='CSEclasses.track'),
        ),
        migrations.AddField(
            model_name='majortech',
            name='major',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CSE_tech', to='Majors.major'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='category21',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category21_CSE_lecture', to='Majors.category'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='category22',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category22_CSE_lecture', to='Majors.category'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='category23',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category23_CSE_lecture', to='Majors.category'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='category24',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category24_CSE_lecture', to='Majors.category'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='tech',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='majortech_CSE_lecture', to='CSEclasses.majortech'),
        ),
    ]
