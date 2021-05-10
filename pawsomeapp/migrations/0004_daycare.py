# Generated by Django 3.1.5 on 2021-02-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pawsomeapp', '0003_pplist'),
    ]

    operations = [
        migrations.CreateModel(
            name='daycare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('location', models.CharField(max_length=100)),
                ('adds', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
