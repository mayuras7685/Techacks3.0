# Generated by Django 4.0.3 on 2022-08-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_counselor_user_is_counselor'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='pincode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
