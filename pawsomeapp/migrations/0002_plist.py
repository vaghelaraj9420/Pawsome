# Generated by Django 3.1.5 on 2021-02-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsomeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('breed', models.CharField(max_length=100)),
                ('offer', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
    ]
