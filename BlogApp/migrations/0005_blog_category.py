# Generated by Django 2.2.3 on 2019-08-04 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0004_auto_20190805_0354'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
    ]