# Generated by Django 4.1 on 2022-08-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_school_standard_hi_school_year_student_std_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='std_id',
        ),
        migrations.AlterField(
            model_name='school',
            name='standard_HI',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
