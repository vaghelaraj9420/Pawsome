# Generated by Django 3.1.5 on 2021-04-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsomeapp', '0019_auto_20210403_1827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caretaker',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='caretaker',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='caretaker',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='caretaker',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='caretaker',
            table=None,
        ),
    ]
