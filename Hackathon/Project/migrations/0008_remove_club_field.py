# Generated by Django 3.2.3 on 2021-07-10 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0007_club_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='field',
        ),
    ]
