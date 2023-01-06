# Generated by Django 4.0.3 on 2022-03-24 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('levelc', models.IntegerField()),
                ('env', models.IntegerField()),
                ('teachersc', models.IntegerField()),
                ('prevdisc', models.IntegerField()),
                ('fecilities', models.IntegerField()),
                ('timetable', models.IntegerField()),
                ('grpwork', models.IntegerField()),
                ('mentalhlth', models.IntegerField()),
                ('sportart', models.IntegerField()),
                ('solveprob', models.IntegerField()),
                ('creativecourse', models.IntegerField()),
                ('foconindv', models.IntegerField()),
                ('mannlearn', models.IntegerField()),
                ('courserele', models.IntegerField()),
                ('issuesofconc', models.IntegerField()),
                ('aresolved', models.IntegerField()),
                ('others', models.CharField(max_length=1000)),
                ('school', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='profiles.school')),
            ],
        ),
    ]
