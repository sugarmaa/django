# Generated by Django 2.2.3 on 2019-08-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0003_chart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='video',
        ),
        migrations.AlterField(
            model_name='blog',
            name='shortNews',
            field=models.CharField(max_length=200),
        ),
    ]