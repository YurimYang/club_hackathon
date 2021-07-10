# Generated by Django 3.1.2 on 2021-07-09 06:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Matching',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_date', models.DateTimeField()),
                ('match_body', models.CharField(max_length=1000)),
                ('club_id', models.ForeignKey(db_column='club_id', on_delete=django.db.models.deletion.CASCADE, to='Project.club')),
            ],
        ),
    ]
