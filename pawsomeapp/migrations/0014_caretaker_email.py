# Generated by Django 3.1.5 on 2021-04-03 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsomeapp', '0013_auto_20210403_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='caretaker',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
    ]
