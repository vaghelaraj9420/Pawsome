# Generated by Django 3.1.5 on 2021-04-12 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsomeapp', '0021_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='caretaker',
            name='experience',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]